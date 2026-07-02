import requests
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Helps enforce HTTPS.",
    "Content-Security-Policy": "Helps prevent Cross-Site Scripting (XSS).",
    "X-Content-Type-Options": "Prevents MIME-type sniffing.",
    "X-Frame-Options": "Protects against clickjacking.",
    "Referrer-Policy": "Controls referrer information.",
    "Permissions-Policy": "Restricts browser features."
}


def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    return "F"


def save_html_report(url, response, results, score, grade):

    filename = "security_report.html"

    html = f"""
<html>
<head>
<title>Security Header Report</title>
<style>
body {{
font-family: Arial;
margin:40px;
background:#f5f5f5;
}}

table {{
border-collapse: collapse;
width:100%;
}}

th,td {{
border:1px solid black;
padding:8px;
}}

.pass {{
color:green;
font-weight:bold;
}}

.fail {{
color:red;
font-weight:bold;
}}
</style>
</head>

<body>

<h1>Security Header Report</h1>

<p><b>Scan Time:</b> {datetime.now()}</p>

<p><b>Target:</b> {url}</p>

<p><b>Final URL:</b> {response.url}</p>

<p><b>Status Code:</b> {response.status_code}</p>

<h2>Security Score: {score:.0f}% ({grade})</h2>

<table>

<tr>

<th>Header</th>

<th>Status</th>

<th>Description</th>

</tr>
"""

    for header, status, description in results:

        css = "pass" if status == "PASS" else "fail"

        html += f"""
<tr>

<td>{header}</td>

<td class="{css}">{status}</td>

<td>{description}</td>

</tr>
"""

    html += """
</table>

</body>

</html>
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    print(Fore.CYAN + f"\nHTML report saved as {filename}")


def check_headers(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        print(Fore.CYAN + "=" * 65)
        print(Fore.CYAN + "CYBERINVINCIBLE SECURITY HEADER CHECKER")
        print(Fore.CYAN + "=" * 65)

        print(f"\nTarget      : {url}")
        print(f"Final URL   : {response.url}")
        print(f"Status Code : {response.status_code}")

        print("\nChecking Security Headers...\n")

        passed = 0
        failed = 0

        results = []

        for header, description in SECURITY_HEADERS.items():

            value = response.headers.get(header)

            if value:

                print(Fore.GREEN + f"[PASS] {header}")

                passed += 1

                results.append((header, "PASS", description))

            else:

                print(Fore.RED + f"[FAIL] {header}")

                failed += 1

                results.append((header, "FAIL", description))

        score = (passed / len(SECURITY_HEADERS)) * 100

        grade = calculate_grade(score)

        print("\n" + "=" * 65)

        print(Fore.YELLOW + "SUMMARY")

        print("=" * 65)

        print(f"Headers Present : {passed}")

        print(f"Headers Missing : {failed}")

        print(f"Security Score  : {score:.0f}%")

        print(f"Grade           : {grade}")

        save_html_report(url, response, results, score, grade)

    except requests.exceptions.RequestException as e:

        print(Fore.RED + str(e))


if __name__ == "__main__":

    website = input("Enter Website URL: ").strip()

    if not website.startswith("http"):
        website = "https://" + website

    check_headers(website)