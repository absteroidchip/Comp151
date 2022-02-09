def main():
    rec_file = open("letterofrec",'r')
    silly_rec = rec_file.readlines()

    line_number = 0
    for line in silly_rec:
        line_number = line_number + 1
        if line_number % 2 == 1:
            print(line)

main()





