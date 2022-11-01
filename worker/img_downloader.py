import gdown

def main():
    url = 'https://drive.google.com/drive/folders/1C9UFaMVp9wkHML32hh7CN2McUUwCoxp5'

    output_path = 'gdrivedata'
    if gdown.download_folder(url, output=output_path, quiet=False, use_cookies=False):
        return "DONE"
    else:
        return "Not working."

if __name__ == "__main__":
    print("="*20+"Start Downloading"+"="*10)
    main()
    print("="*20+"End"+"="*10)
