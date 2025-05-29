from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(["username", "password"])
ws.append(["Admin", "admin123"])
ws.append(["fakeuser", "fakepass"])
ws.append(["Admin", "wrongpass123"])
wb.save("credentials.xlsx")
