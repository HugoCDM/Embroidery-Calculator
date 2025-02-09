wwwwwww# Embroidery Calculator
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p> A Tkinter-based application for calculating embroidery costs based on quantity and type of logo. This project was developed for a Brazilian uniform company</p>




## 📥 Installation
1. Clone the repository and navigate into the directory
   ```bash
   git clone https://github.com/HugoCDM/Embroidery-Calculator.git
   cd Embroidery-Calculator
   ```
2. Create and activate a virtual environment(optional)
   ```bash
   python -m venv venv 
   .\venv\Scripts\activate 
   ```
3. Install the dependencies -requirements
   ```bash
   pip install -r requirements.txt 
   ```
If you have trouble with .\venv\Scripts\activate, run Windows PowerShell on your search bar as an administrator and write:
```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser # Then type Y and press Enter. Go to step 2
```
## 🖱 Usage
### 1. Quantity area(Quantidade)
- You must type how many items you are going to embroider
### 2. Embroidery value area(Valor Bordado)
- It's a combobox which contains 6 types of logo and their corresponding values

### 3. Buttons and Functionalities
#### 3.1 Enviar Button
- Once you click on enviar button, the magic happens. It calls the send() function which has some ifs. Depending on your quantity of items it has different outputs.
- Clears the entry area calling the function clear().

## ƒ Functions
### main()
- The main window

### combos(eventObject)
- combo_get: stores the selected embroidery type.

### send()
- Gets the input value from <b>*qtd = entry_qty.get()*</b>
- Calls the combos() function getting the selected combobox option
- Shows the corresponding value on <b>*label_result_text_area*</b> after clicked 

### clear()
- Clears the entry area


## 🌅 Image section

![embroidery](https://github.com/user-attachments/assets/34de65d9-9436-46e7-b8eb-c2d2a0ff88f9)

### *Made by [Hugo Mello](https://github.com/HugoCDM)*







