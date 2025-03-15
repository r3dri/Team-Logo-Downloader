import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, X, BOTH, END
from threading import Thread

class TeamLogoDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Team Logo Downloader")

        self.url_label = ttk.Label(master, text="URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.url_entry = ttk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.url_entry.insert(0, "https://www.vscl.ru/tournaments/868/participants")

        self.output_label = ttk.Label(master, text="Выберите папку сохранения:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.output_path = tk.StringVar()
        self.output_path.set("teams_img")

        self.browse_button = ttk.Button(master, textvariable=self.output_path, command=self.browse_folder, width=50)
        self.browse_button.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        self.filename_label = ttk.Label(master, text="Выберите тип названия:")
        self.filename_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.filename_type = tk.StringVar(value="Полное")
        self.filename_combo = ttk.Combobox(master, textvariable=self.filename_type, values=["Полное", "Сокращенное"], state="readonly")
        self.filename_combo.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.download_button = ttk.Button(master, text="Выгрузить логотипы", command=self.start_download)
        self.download_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.status_label = ttk.Label(master, text="")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)

        master.columnconfigure(1, weight=1)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_path.set(folder_selected)

    def start_download(self):
        url = self.url_entry.get()
        output_dir = self.output_path.get()
        filename_type = self.filename_type.get()
        Thread(target=self.download_team_logos_threaded, args=(url, output_dir, filename_type)).start()

    def download_team_logos_threaded(self, url, output_dir,filename_type):
        try:
            self.download_team_logos(url, output_dir, filename_type)
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")


    def download_team_logos(self, url, output_dir="teams_img",filename_type="Полное"):
        self.status_label.config(text="Starting download...")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            team_divs = soup.find_all("div", class_="col-2 mb-3")

            total_teams = len(team_divs)
            for i, team_div in enumerate(team_divs):
                a_tag = team_div.find("a")
                if a_tag and "href" in a_tag.attrs:
                    team_url_relative = a_tag["href"]
                    team_url = urljoin(url, team_url_relative)

                    try:
                        team_response = requests.get(team_url)
                        team_response.raise_for_status()
                        team_soup = BeautifulSoup(team_response.content, "html.parser")

                        if filename_type == "Полное":
                            team_name_span = team_soup.find("span", class_="vcard-nickname d-block")
                        elif filename_type == "Сокращенное":
                            team_name_span = team_soup.find("span", class_="vcard-fullname d-block")
                        else:
                            self.status_label.config(text="Error: Invalid filename type selected.")
                            continue

                        if team_name_span:
                            team_name = team_name_span.text.strip()
                        else:
                            self.status_label.config(text=f"Error: Team name not found on {team_url}")
                            continue

                        logo_div = team_soup.find("div", class_="vcard-logo")
                        if logo_div:
                            img_tag = logo_div.find("img", class_="w-100")
                            if img_tag and "src" in img_tag.attrs:
                                logo_url = urljoin(team_url, img_tag["src"])
                            else:
                                self.status_label.config(text=f"Error: Logo URL not found on {team_url}")
                                continue
                        else:
                            self.status_label.config(text=f"Error: Logo div not found on {team_url}")
                            continue

                        try:
                            logo_response = requests.get(logo_url)
                            logo_response.raise_for_status()
                            image = Image.open(BytesIO(logo_response.content))
                            filename = os.path.join(output_dir, f"{team_name}.png")

                            image.save(filename, "PNG")
                            self.status_label.config(text=f"Downloaded {i+1}/{total_teams}: {team_name}")
                            self.master.update()
                        except requests.exceptions.RequestException as e:
                            self.status_label.config(text=f"Error downloading logo from {logo_url}: {e}")
                        except Exception as e:
                            self.status_label.config(text=f"Error processing image for {team_name}: {e}")

                    except requests.exceptions.RequestException as e:
                        self.status_label.config(text=f"Error requesting team page {team_url}: {e}")
                else:
                    self.status_label.config(text="Error: No <a> tag found.")
        except requests.exceptions.RequestException as e:
            self.status_label.config(text=f"Error requesting participants page {url}: {e}")

        self.status_label.config(text="Download complete!")

root = tk.Tk()
gui = TeamLogoDownloaderGUI(root)
root.mainloop()