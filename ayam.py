import requests
import time

url = 'https://api.chickcoop.io/hatch/manual'
common_headers = {
    'authority': 'api.chickcoop.io',
    'origin': 'https://game.chickcoop.io',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
}

def send_request(auth_header):
    headers = common_headers.copy()
    headers['authorization'] = auth_header
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        try:
            response_json = response.json()
            if response_json.get('ok') and response_json.get('data'):
                quantity = response_json['data']['chickens']['quantity']
                username = response_json['data']['profile']['username']
                print(f"[ #{username} ] BERHASIL NETESIN TELOR, AYAM SEKARANG {quantity}")
        except ValueError:
            print("Gagal memparsing JSON dari respons")
    else:
        print(f"Gagal mengirim permintaan, Status Code: {response.status_code}, Response: {response.text}")

def main():
    with open('query.txt', 'r') as file:
        auth_data = [line.strip() for line in file if line.strip()]

    while True:
        for auth_header in auth_data:
            send_request(auth_header)
        time.sleep(1)

if __name__ == "__main__":
    main()
