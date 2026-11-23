import flet as ft
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(amount, from_currency, to_currency):
    data = requests.get(API_URL).json()
    rates = data["rates"]
    
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("https://api.exchangerate-api.com/docs/supported-currencies")
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]
    return converted_amount

def main(page: ft.Page):
    page.title = "konverter mata uang"
    page.window_width = 320
    page.window_height = 380
    page.padding = 20

    amount_input = ft.TextField(label="Jumlah", value="1", width=280)
    from_currency_input = ft.TextField(label="Mata Uang Asal (e.g., USD)", value="USD", width=280)
    to_currency_input = ft.TextField(label="Mata Uang Tujuan (e.g., EUR)", value="EUR", width=280)
    result_text = ft.Text(value="", 
                          size=26,
                          weight=ft.FontWeight.BOLD)
    def convert_click(e):
        try:
            amount = float(amount_input.value)
            from_currency = from_currency_input.value.upper()
            to_currency = to_currency_input.value.upper()
            converted_amount = convert_currency(amount, from_currency, to_currency)
            result_text.value = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        except ValueError as ve:
            result_text.value = str(ve)
        except Exception as e:
            result_text.value = "Error: " + str(e)
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text("Konverter Mata Uang", size=24, weight=ft.FontWeight.BOLD),
                amount_input,
                from_currency_input,
                to_currency_input,
                ft.Button("Convert", on_click=convert_click, width=280),
                result_text
            ],
            spacing=15,
        )
    )
ft.run(main)