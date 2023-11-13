while True:    
    print("Please enter the word to be censored: ")
    censor = input("(!) ")
    censorL = len(censor)
    censored = censor.replace(censor, ("*" * len(censor)))
    while True:
        print("Please enter the name of the file to be viewed: ")    
        filename = input("> ")    
        try:        
            with open(filename) as file:          
                content = file.read()  
                content = content.replace(censor, censored)
                print(content)
            break
        except OSError:        
            print("There was a problem working with this file.")
    break