import speedtest
import socket
import uuid

def Internet_Speed_Test():
    print("Wait a Minute, Testing your internet speed...")

    Speed_Test = speedtest.Speedtest()
    best_server = Speed_Test.get_best_server()



    
    server_country = best_server['country']
    latency = best_server['latency']
    isp_name = Speed_Test.config['client']['isp']
    ip_address = Speed_Test.config['client']['ip']
    country = Speed_Test.config['client'].get('country', 'Unknown Country')
    


    download_speed = (Speed_Test.download() / 1_000_000) / 8
    upload_speed = (Speed_Test.upload() / 1_000_000) / 8

    print("\n------ Internet Speed Test Results ------\n")

    print(f"Download Speed: {download_speed:.2f} MBps")
    print(f"Upload Speed: {upload_speed:.2f} MBps") 



    print(f"Server Country: {server_country}")
    print(f"Latency: {latency}")
    print(f"ISP: {isp_name}")
    print(f"IP Address: {ip_address}")
    print(f"ISP Location: {country}")
    
if __name__ == "__main__":
    Internet_Speed_Test()