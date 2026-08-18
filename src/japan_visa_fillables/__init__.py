from .cv import create_cv
from .outline_activities import create_outline_activities

def main():
    print("Generating Resume/CV PDF...")
    create_cv()
    print("Generating Outline of Intended Activities PDF...")
    create_outline_activities()
    print("Done! Both PDFs generated successfully.")

if __name__ == "__main__":
    main()