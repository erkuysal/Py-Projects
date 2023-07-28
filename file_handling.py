class SaveData:
    def __init__(self,file_name):
        self.file_name = file_name

    def write_data(self,data):
        mode = 'a' if self.if_exists() else 'w'
        with open(self.file_name, mode) as file:
            file.write(data + '\n')

    def if_exists(self):
        try:
            # Try to open the file in read mode to check if it exists
            with open(self.file_name, "r"):
                print('! Data Added !')
                pass
            return True
        except FileNotFoundError:
            print('! File Created !')
            return False


data = 'test sentence.'
file_name = 'test.txt'

save_data = SaveData(file_name)
save_data.write_data(data)


