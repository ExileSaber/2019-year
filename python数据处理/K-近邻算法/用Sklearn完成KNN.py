import pandas as pd
from sklearn.preprocessing import StandardScaler

# 获取需要的数据
features = ['accommodates', 'bedrooms', 'bathrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights',
            'number_of_reviews']
dc_listings = pd.read_csv('listings.csv')
dc_listings = dc_listings[features]

# 数据可视化及可操作化处理
dc_listings['price'] = dc_listings.price.str.replace("\$|,", '').astype(float)
dc_listings = dc_listings.dropna()
dc_listings[features] = StandardScaler().fit_transform(dc_listings[features])
normalized_listings = dc_listings

print('数据规模及其前五个数据列表')
print(dc_listings.shape)  # 数据处理完成后的数据规模
print(normalized_listings.head())  # 输出前五行

norm_train_df = normalized_listings.copy().iloc[0:2792]  # 训练集（深复制）
norm_test_df = normalized_listings.copy().iloc[2792:]  # 测试集

# 两点之间'距离'计算方法
from scipy.spatial import distance
first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
fifth_listing = normalized_listings.iloc[20][['accommodates', 'bathrooms']]
first_fifth_distance = distance.euclidean(first_listing, fifth_listing)  #调用库distance中两点之间运算距离的方法euclidean（）
print('两点间距')
print(first_fifth_distance)


# 多变量KNN模型
def predict_price_multivariate(new_listing_value, feature_columns):
    temp_df = norm_train_df
    temp_df['distance'] = distance.cdist(temp_df[feature_columns], [new_listing_value[feature_columns]])  #cdist()计算的就是两个向量之间的metric距离度量（第二个参数写法不清楚为什么）
    temp_df = temp_df.sort_values('distance')  #根据distance指标由小到大排序
    knn_5 = temp_df.price.iloc[:5]  #price列通过iloc根据行号索引取前五行的数值
    predicted_price = knn_5.mean()  #再取平均值
    return predicted_price  #相当于预测值


cols = ['accommodates', 'bathrooms']
norm_test_df['predicted_price'] = norm_test_df[cols].apply(predict_price_multivariate, feature_columns=cols, axis=1)  #用apply方法调用函数，axis=1表示行

#求RMSE（均方根误差）
norm_test_df['squared_error'] = (norm_test_df['predicted_price'] - norm_test_df['price']) ** 2  #这里需要使用实验集norm_test_df['price']
mse = norm_test_df['squared_error'].mean()
rmse = mse ** (1 / 2)

print(rmse)


#Sklearn方法（双特征）
from sklearn.neighbors import KNeighborsRegressor
cols = ['accommodates', 'bedrooms']  #设置要处理的数据所在的行
knn = KNeighborsRegressor()  #实例化
knn.fit(norm_train_df[cols], norm_train_df['price'])  #将第一个参数作为训练数据，将第二个参数作为调整数据
two_features_predictions = knn.predict(norm_test_df[cols])  #预测所提供数据的目标

#求RMSE（均方根误差）
from sklearn.metrics import mean_squared_error
two_features_mse = mean_squared_error(norm_test_df['price'], two_features_predictions)  #平均平方误差回归损失，这里需要使用实验集norm_test_df['price']
two_features_rmse = two_features_mse ** (1/2)
print(two_features_rmse)

#Sklearn方法（多特征）
knn = KNeighborsRegressor()
cols = ['accommodates', 'bedrooms', 'bathrooms', 'beds', 'minimum_nights', 'maximum_nights', 'number_of_reviews']
knn.fit(norm_train_df[cols], norm_train_df['price'])  #将第一个参数作为训练数据，将第二个参数作为调整数据
four_features_predictions = knn.predict(norm_test_df[cols])  #预测所提供数据的目标
four_features_mse = mean_squared_error(norm_test_df['price'], four_features_predictions)  #平均平方误差回归损失，这里需要使用实验集norm_test_df['price']
four_features_rmse = four_features_mse ** (1/2)
print(four_features_rmse)
