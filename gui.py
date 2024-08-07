# gui.py
import tkinter as tk
from tkinter import filedialog
from functions import load_excel
import pandas as pd
import re

class DuplicatesRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eliminador de Duplicados en Excel")

        self.filename = None
        self.output_folder = None

        # Botón para seleccionar el archivo
        self.file_button = tk.Button(root, text="Seleccionar Archivo Excel", command=self.select_file)
        self.file_button.pack()

        # Etiqueta y Campo para el nombre del archivo de salida
        self.output_label = tk.Label(root, text="Nombre del archivo de salida:")
        self.output_label.pack()
        self.output_entry = tk.Entry(root)
        self.output_entry.pack()

        # Botón para seleccionar la carpeta de salida
        self.folder_button = tk.Button(root, text="Seleccionar Carpeta de Salida", command=self.select_folder)
        self.folder_button.pack()

        # Etiqueta para mostrar el estado del proceso
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

        # Botón para procesar el archivo
        self.process_button = tk.Button(root, text="Eliminar Duplicados", command=self.process_file)
        self.process_button.pack()

        # Texto para mostrar resultados
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def select_file(self):
        try:
            self.filename = filedialog.askopenfilename()
            if self.filename:
                df = load_excel(self.filename)
                if df is not None:
                    columns = df.columns.tolist()
                    print(f"Columnas encontradas: {columns}")  # Mensaje de depuración
                    if 'NOM' in columns and 'MAIL CONTACTE' in columns and 'MAIL' in columns:
                        print("Columnas necesarias presentes.")
                    else:
                        print("Faltan columnas necesarias en el archivo.")
                else:
                    print("Error al cargar el archivo. Asegúrate de que el archivo tenga datos y esté en el formato correcto.")
            else:
                print("No se seleccionó ningún archivo.")
        except Exception as e:
            print(f"Error al seleccionar el archivo: {e}")

    def select_folder(self):
        try:
            self.output_folder = filedialog.askdirectory()
        except Exception as e:
            print(f"Error al seleccionar la carpeta: {e}")

    def process_file(self):
        if not self.filename or not self.output_folder:
            print("Archivo de entrada o carpeta de salida no seleccionados.")
            self.status_label.config(text="Error: Archivo o carpeta no seleccionados.")
            return
        
        output_filename = self.output_entry.get()
        if not output_filename:
            print("Por favor, proporciona un nombre para el archivo de salida.")
            self.status_label.config(text="Error: Nombre de archivo de salida no proporcionado.")
            return

        self.status_label.config(text="En proceso...")
        self.root.update_idletasks()  # Actualiza la interfaz gráfica

        df = load_excel(self.filename)
        if df is not None:
            try:
                # Considerar solo las columnas relevantes
                relevant_columns = ['NOM', 'MAIL CONTACTE', 'MAIL']
                df = df[relevant_columns]

                # Lista para almacenar las filas con emails únicos
                data = []
                duplicates = set()
                invalid_emails = set()
                unique_emails_set = set()

                # Regex para validar emails
                email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

                for _, row in df.iterrows():
                    emails = set()
                    if pd.notna(row['MAIL CONTACTE']):
                        if email_pattern.match(row['MAIL CONTACTE']):
                            if row['MAIL CONTACTE'] in unique_emails_set:
                                duplicates.add(row['MAIL CONTACTE'])
                            else:
                                unique_emails_set.add(row['MAIL CONTACTE'])
                                emails.add(row['MAIL CONTACTE'])
                        else:
                            invalid_emails.add(row['MAIL CONTACTE'])
                    if pd.notna(row['MAIL']):
                        if email_pattern.match(row['MAIL']):
                            if row['MAIL'] in unique_emails_set:
                                duplicates.add(row['MAIL'])
                            else:
                                unique_emails_set.add(row['MAIL'])
                                emails.add(row['MAIL'])
                        else:
                            invalid_emails.add(row['MAIL'])

                    for email in emails:
                        data.append({'NOM': row['NOM'], 'email_final': email})

                df_unique_emails = pd.DataFrame(data)

                # Eliminar duplicados basados en 'email_final'
                df_unique_emails.drop_duplicates(subset=['email_final'], inplace=True)

                output_path = f"{self.output_folder}/{output_filename}.xlsx"
                df_unique_emails.to_excel(output_path, index=False)
                print(f"Archivo guardado en: {output_path}")
                self.status_label.config(text="Completado")

                # Resumen de la operación
                duplicates_count = len(duplicates)
                invalid_emails_count = len(invalid_emails)
                total_valid_emails = df_unique_emails.shape[0]

                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Emails duplicados encontrados y eliminados: {duplicates_count}\n")
                self.result_text.insert(tk.END, f"Emails con formato incorrecto eliminados: {invalid_emails_count}\n")
                self.result_text.insert(tk.END, f"Total de emails válidos: {total_valid_emails}\n")

                # Mostrar lista de duplicados e inválidos si es necesario
                self.result_text.insert(tk.END, "\nEmails duplicados:\n")
                self.result_text.insert(tk.END, ", ".join(duplicates) + "\n")
                self.result_text.insert(tk.END, "\nEmails con formato incorrecto:\n")
                self.result_text.insert(tk.END, ", ".join(invalid_emails) + "\n")

            except Exception as e:
                print(f"Error al guardar el archivo: {e}")
                self.status_label.config(text="Error: No se pudo guardar el archivo.")
        else:
            self.status_label.config(text="Error al procesar el archivo.")

# Código para inicializar la aplicación desde main.py
if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicatesRemoverApp(root)
    root.mainloop()
