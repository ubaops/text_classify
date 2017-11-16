from ci_seg import *
from tfidf_train import *
from to_bunch import *

#训练传入训练字典
'''
1:品牌
2:价格
3:项目简介
4:效果
'''
train_set={
        '品牌':["厨房橱柜","无锡装修公司","月星家居","实木床","青山厨柜","实木复合地板","无锡建材市场在哪里","无锡华夏家居港","实木门","华夏家居港","木门十大名牌有哪些","橱柜品牌","瓷砖品牌","地板品牌","东鹏瓷砖","复合地板十大排名","樱花木门是几线品牌","马桶品牌排行榜","国内十大马桶品牌","十大卫浴品牌"],
        '价格':["实木门价格","红酸枝家具价格","一套威法橱柜要多少钱","无锡双11建材那里有优惠活动","木地板价格","优格橱柜多少钱一平米","橡木地板的价格","红酸枝家具大降价","一般实木门价格","整体卫生间价格多少","toto马桶价格","toto智能马桶价格","索非亚衣柜价格","白酸枝一套家具多少钱","红酸枝的价格","无锡买家具哪里便宜"],
        '项目简介':["无锡家装节2017","无锡家装节","家博会","无锡家装博览会","无锡家博会","无锡2012年10月15日家博会","2017无锡家装博览会","2017无锡新体家装节","无锡建材团购活动","无锡新体家装节","兔狗家装节","无锡广电家博会","无锡广电家装节2017","家装节","2017无锡家装节","2017无锡广电家装节","无锡家博会2017","无锡家装博览会2016","2017无锡家装节时间","2017无锡太湖博览中心家装节"],
        '效果':["卫生间装修效果图","客厅装修效果图","装修效果图","客厅背影墙装修效果图","地板砖效果图","窗帘效果图","复式楼装修效果图","餐厅装修效果图","开放式厨房装修效果图","装潢效果图"]}
#分词路径
seg_path = "./clickplus_train_seg/"  # 分词后分类语料库路径  
#进行分词
corpus_segment(train_set,seg_path) 

#对训练集进行Bunch化操作：  
wordbag_path = "train_word_bag/train_set.dat"  # Bunch存储路径  
seg_path = "clickplus_train_seg/"  # 分词后分类语料库路径  
corpus2Bunch(wordbag_path, seg_path)

#词向量训练
stopword_path = "train_word_bag/hlt_stop_words.txt"#停用词表的路径  
bunch_path = "train_word_bag/train_set.dat"  #导入训练集Bunch的路径  
space_path = "train_word_bag/tfdifspace.dat"  # 词向量空间保存路径  
vector_space(stopword_path,bunch_path,space_path)