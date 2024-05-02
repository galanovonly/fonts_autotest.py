from selenium import webdriver                                  # нажимаем "запуск" (shift+F10) - открывается страница, вводим имя и пароль вручную (60 секунд на ввод)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from expected_fonts_PROJECT import *


def find_elements_by_font_size(driver, font_size):
    script = """
    var matchingElements = [];
    var allElements = document.getElementsByTagName('*');

    for (var i = 0; i < allElements.length; i++) {
        var elem = allElements[i];
        if (window.getComputedStyle(elem).fontSize === arguments[0]) {
            matchingElements.push(elem);
        }
    }

    return matchingElements;
    """
    elements = driver.execute_script(script, font_size)
    # Convert JavaScript elements to Selenium elements
    return [driver.execute_script("return arguments[0];", element) for element in elements]


def check_font_properties(element):
    font_size = element.value_of_css_property('font-size')
    font_family = element.value_of_css_property('font-family')
    font_weight = element.value_of_css_property('font-weight')
    color = element.value_of_css_property('color')
    return font_size, font_family, font_weight, color


def is_font_size_within_tolerance(actual, expected, tolerance=0.5):
    actual_size = float(actual.rstrip('px'))
    expected_size = float(expected.rstrip('px'))
    return abs(actual_size - expected_size) <= tolerance


def normalize_font_name(font_name):
    return font_name.lower().replace('"', '').replace("'", '').replace(' ', '')

def has_matching_font_family(actual, expected):
    # Normalize the font names by removing quotes, spaces, and making them lower case for comparison
    actual_normalized = [normalize_font_name(font) for font in actual.split(',')]
    expected_normalized = [normalize_font_name(font) for font in expected.split(',')]

    # Check if any version of the expected font family is present in the actual font family list
    return any(expected_font in actual_normalized for expected_font in expected_normalized)


def report_discrepancies(element_html, element_type, actual_styles, expected_styles, resolution):
    discrepancies = []
    resolution_str = f"{resolution['width']}x{resolution['height']}"

    # Check 'font-size' discrepancy
    if not is_font_size_within_tolerance(actual_styles['font-size'], expected_styles['font-size']):
                            # f"Actual {actual_styles['font-size']}, Expected {expected_styles['font-size']} font size incorrect at '{element_html}' {resolution_str}"
        discrepancy_msg = f"ACTUAL {actual_styles['font-size']}, EXPECTED {expected_styles['font-size']} on {resolution_str} FONT SIZE incorrect at '{element_html}'" # f"Font size incorrect at '{element_html}' {resolution_str}: Actual {actual_styles['font-size']}, Expected {expected_styles['font-size']}"
        discrepancies.append(discrepancy_msg)

    # Check 'font-family' discrepancy
    if not has_matching_font_family(actual_styles['font-family'], expected_styles['font-family']):
                            # f"Actual {actual_styles['font-family']}, Expected {expected_styles['font-family']} font family incorrect at '{element_html}' {resolution_str}"
        discrepancy_msg = f"ACTUAL {actual_styles['font-family']}, EXPECTED {expected_styles['font-family']} on {resolution_str} FONT FAMILY incorrect at '{element_html}'" # f"Font family incorrect at '{element_html}' {resolution_str}: Actual {actual_styles['font-family']}, Expected {expected_styles['font-family']}"
        discrepancies.append(discrepancy_msg)

    # Add other checks here (e.g., 'font-weight', 'color') if needed

    return discrepancies


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)

all_discrepancies = []

for element_type in element_types:
    try:
        elements = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, f"//*[contains(@class, '{element_type}')]")))
    except TimeoutException:
        print(f"\nNo elements found for {element_type} by class, searching by font size...")
        expected_font_size_1920 = expected_fonts[element_type]['1920']['font-size']
        elements = find_elements_by_font_size(driver, expected_font_size_1920)
    if not elements:
        print(f"No elements found with font size {expected_font_size_1920} for {element_type}.")
        continue

    for element in elements:
        print("\n" + url)
        element_html = element.get_attribute('outerHTML')
        print(element_html)
        print(f'{element_type}')

        for device_metrics in resolutions:
            resolution_key = str(device_metrics['width'])  # Correct variable name
            font_style = expected_fonts[element_type][resolution_key]  # Corrected to use resolution_key

            print(f"                    ◻◻◻{device_metrics['width']}x{device_metrics['height']}◻◻◻")
            driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", device_metrics)
            time.sleep(0.5)  # Small delay to let the browser adjust to the new resolution

            font_size, font_family, font_weight, color = check_font_properties(element)  # Corrected to use 'element'
            actual_styles = {
                'font-size': font_size,
                'font-family': font_family,
                'font-weight': font_weight,
                'color': color
            }

            discrepancies = report_discrepancies(element_html, element_type, actual_styles, font_style, device_metrics)
            all_discrepancies.extend(discrepancies)

            # Print actual and expected values for each property
            print("Actual  : ", end="")
            if 'font-size' in font_style:
                print(f"{font_size}, ", end="")
            if 'font-family' in font_style:
                print(f"{font_family}, ", end="")
            if 'font-weight' in font_style:
                print(f"{font_weight}, ", end="")
            if 'color' in font_style:
                print(f"{color}, ", end="")

            print("\nExpected: ", end="")
            if 'font-size' in font_style:
                print(f"{font_style['font-size']}, ", end="")
            if 'font-family' in font_style:
                print(f"{font_style['font-family']}, ", end="")
            if 'font-weight' in font_style:
                print(f"{font_style['font-weight']}, ", end="")
            if 'color' in font_style:
                print(font_style['color'], end="")

            print()  # Move to the next line after printing all properties

# Print all discrepancies found
if all_discrepancies:
    print("\nDiscrepancies found:")
    print(url)
    for discrepancy in all_discrepancies:
        print(discrepancy)
else:
    print("\nNo discrepancies found.")

# time.sleep(300)
driver.quit()

output_filename = "output.txt"

with open(output_filename, "w") as f:
    for discrepancy in all_discrepancies:
        f.write(discrepancy + "\n")

print(f"Results saved to {output_filename}")
