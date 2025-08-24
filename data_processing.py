class data_show:

    def clock_form(video_list_clock,clock):

        if video_list_clock.count(clock)==0:
            return 1
        elif video_list_clock.count(clock)<4:
            return 2
        elif video_list_clock.count(clock)<7:
            return 3
        elif video_list_clock.count(clock)<10:
            return 4
        elif video_list_clock.count(clock)>=10:
            return 5

    def video_rating(video_api):

        view=video_api.get("view")

        view_rating=view/(video_api.get("sub")**0.8*12)
        like_rating=video_api.get("like")/(view*0.06)
        coin_rating=video_api.get("coin")/(view*0.015)
        favorite_rating=video_api.get("favorite")/(view*0.04)
        share_rating=video_api.get("share")/(view*0.005)
        reply_rating=video_api.get("reply")/(view*0.003)
        danmaku_rating=video_api.get("danmaku")/(view*0.001)

        rating_list=[view_rating,like_rating,coin_rating,favorite_rating,share_rating,reply_rating,danmaku_rating]
        rating_list_check=[]

        for rating in rating_list:
            if rating>1:
                rating=1
            rating_list_check.append(rating)

        rating_all=rating_list_check[0]*0.5+rating_list_check[1]*0.08+rating_list_check[2]*0.1+rating_list_check[3]*0.1+rating_list_check[4]*0.02+rating_list_check[5]*0.15+rating_list_check[6]*0.05

        if rating_all>0.85:
            rank,color="S","245,193,54"
        elif rating_all>0.75:
            rank,color="A","245,54,94"
        elif rating_all>0.6:
            rank,color="B","225,54,245"
        elif rating_all>0.4:
            rank,color="C","49,142,221"
        elif rating_all<=0.4:
            rank,color="D","49,221,138"

        rating_show=[rating_all,rank,color]
            
            

        return rating_show

            
        
        
        
        

            
        
