import backend
import frontend

def main():
    data = backend.get_data()
    processed_data = backend.process_data(data)
    frontend.display_data(processed_data)

if __name__ == "__main__":
    main()
