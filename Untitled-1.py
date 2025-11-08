with("openfile.csv","r",newline = " "):
    y = f.readlines()
    m = 0
    emp_rec = None
    
    for line in y:
        l = line.strip().split(",")
        if int(l[4])>m:
            m = int(l[4])
            emp_rec= l


       
