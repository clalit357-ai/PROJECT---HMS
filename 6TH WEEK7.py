blog_dict={"Post1":['python','ai','ml'],'Post2':['ai','datascience','python'],'Post3':['ml','ai','cloud']}
dict_2={}
dict_3={}
dict_4={}
dict_5={}
for title,tags in blog_dict.items():
    for tag in tags:
        if tag not in dict_2:
            dict_2[tag]=[title]
        else:
            dict_2[tag].append(title)
    for key,value in dict_2.items():
        dict_3={key:len(value)}
        dict_4.update(dict_3)
    print(dict_4)
    def tag_stats():
        sum=0
        post_no=len(blog_dict)
        for key,value in dict_4.items():
            sum+=value
        dict_5.update(dict_4)
        for key,value in dict_5.items():
            dict_5[key]=(value/post_no)*100
        print(dict_5)
    tag_stats()


            
                

