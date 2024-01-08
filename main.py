import sys
import views


def main():

    if len(sys.argv) == 2:
        argument = sys.argv[1]


        if argument == "graphic":
            import pygameview
            pygameview.screen_loader()
            pygameview.main_menu()
            print("Hello World!")
        elif argument == "ascii":
            views.screenchanger()
        else:
            print("Zły argument")
            sys.exit(1)
    else:
        print("Brak wymaganego argumentu")
        sys.exit(1)

if __name__ == '__main__':
    main()

