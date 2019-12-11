
def functionException(fileName):
    try:
        #raise("Wrong denominator given")
        temp = open(fileName)
        assert temp.read() == None
        print()
        a = 5
    except FileNotFoundError as ex:
        print(ex)
    except Exception as e:
        print("error occurred ==> ", e)
    else:
        print(temp.read())
        temp.close()
        print("Good, file found")
    finally:
        print("Closing connection")

functionException("File0")
