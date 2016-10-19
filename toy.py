# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
fushan_story = media.Movie('釜山行','城市四处出现了丧尸，列车里的乘客求生的故事','https://img3.doubanio.com/view/photo/photo/public/p2345980276.jpg','https://movie.douban.com/trailer/200704/#content')
meigong_story = media.Movie('湄公河行动 ','中国商船在湄公河金三角水域遭遇袭击,警方打击毒贩的故事','https://img3.doubanio.com/view/photo/photo/public/p2379928605.jpg','https://movie.douban.com/trailer/204205/#content')
amelie = media.Movie('天使爱美丽','艾米莉的浪漫爱情故事','https://img3.doubanio.com/view/photo/thumb/public/p803929482.jpg','http://v.qq.com/x/cover/o9ltjk5yc26z6w9.html?ptag=douban.movie')
#amelie.show_trailer()
movies = [fushan_story,meigong_story,amelie]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__module_)
print(media.Movie.__name__)

