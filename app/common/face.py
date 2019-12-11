# _*_ coding: utf-8 _*_
import dlib
import os
import datetime
import uuid
import  face_recognition
from PIL import Image,ImageDraw
#人脸识别小程序
from cv2 import cv2


class Face:
    #定义初始化构造方法
    def __init__(self,directory_path,picture_name,save_path):
        self.dir_path = directory_path
        self.pic_name = picture_name
        self.save_path = save_path
    #时间
    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    #保存名称定义
    @property
    def image_name(self):
        #名称构成：时间+唯一字符串
        prefix1 = self.dt
        prefix2 = uuid.uuid4().hex
        return prefix1+prefix2

    #保存识别的结果
    def save_pil_face(self,pil_image):
        #如果保存的目录不存在，则创建
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        #定义完整的图片路径
        filename = "{}.png".format(
            self.image_name
        )
        #保存到指定位置
        pil_image.save(
            os.path.join(
                self.save_path,filename
            ),
            'png'
        )
        return filename
    #图片初始化
    @property
    def image_init(self):
        image = face_recognition.load_image_file(
            os.path.join(
                self.dir_path,
                self.pic_name
            )
        )
        return image




    #获取图象中人脸的位置
    def get_face_location(self):
        #加载图片
        image = self.image_init
        face_locations = face_recognition.face_locations(image)
        return image,face_locations


    #获取人脸的特征
    def get_face_landmarks(self):
        #获取图片
        image = self.image_init
        #通过特征算法获取所有的特征点
        face_landmarks_list = face_recognition.face_landmarks(image)
        return image, face_landmarks_list

    #框选人脸
    def face_box(self):
        #获取人脸的位置
        image,face_locations = self.get_face_location()
        #将图片转化为图像数组
        pil_image = Image.fromarray(image)
        #把图像数组转化为可绘制的对象
        draw = ImageDraw.Draw(pil_image)
        #循环遍历人脸上下左右的文职
        for (top,right,bottom,left) in face_locations:
            #绘制边框
            draw.rectangle(
                (
                    (left,top),
                    (right,bottom)
                ),
                outline=(0,0,255)
            )
            # pil_image.show()
        #保存图像
        filename =  self.save_pil_face(pil_image)
        return [filename]
    #人脸勾勒功能
    def face_sense(self):
        #获取凸显共和人脸特征
        image,face_landmarks_list = self.get_face_landmarks()
        facial_features = [
            'chin',
            'left_eyebrow',
            'right_eyebrow',
            'nose_bridge',
            'nose_tip',
            'left_eye',
            'right_eye',
            'top_lip',
            'bottom_lip'
        ]
        #将图片转化为图像数组
        pil_image = Image.fromarray(image)
        #将图片变成可绘制对象
        draw = ImageDraw.Draw(pil_image)

        #遍历所有的特征点
        for face_landmark in face_landmarks_list:
            #遍历特征列表
            for facial_feature in facial_features:
                #绘制描线
                draw.line(face_landmark[facial_feature],width=4,fill=(255,255,255))
        # pil_image.show()
        #保存图像
        filename = self.save_pil_face(pil_image)
        return [filename]
    #人脸截取功能
    def face_find(self):
        #获取图像和人脸的位置
        image,face_locations = self.get_face_location()
        result = []
        #循环遍历人脸的位置
        for face_location in face_locations:
            #获取上下左右的位置
            top,right,bottom,left = face_location
            #框选图片中所有人脸的位置
            face_image = image[top:bottom,left:right]
            # 把框选出来的结果，转化为图片数组
            pil_image = Image.fromarray(face_image)
            #保存图片
            filename = self.save_pil_face(pil_image)
            #把最终的结果追加到头像列表中
            result.append(
                filename
            )
        return result
    #人脸化妆
    def face_makeup(self):
        #获取图像和人脸的位置
        image, face_landmarks_list = self.get_face_landmarks()
        print(face_landmarks_list)
        #将图像转化为图像数组
        pil_image = Image.fromarray(image)
        #将图像数组转化为可绘制的对象
        draw = ImageDraw.Draw(pil_image,'RGBA')
        #循环遍历人脸的特征
        for face_landmark in face_landmarks_list:
            #绘制眉毛
            draw.polygon(face_landmark['left_eyebrow'],fill=(68,54,39,128))
            draw.polygon(face_landmark['right_eyebrow'], fill=(68, 54, 39, 128))
            draw.line(face_landmark['left_eyebrow'], fill=(68, 54, 39, 128),width=5)
            draw.line(face_landmark['right_eyebrow'], fill=(68, 54, 39, 128),width=5)

            #绘制嘴唇,太可怕了
            draw.polygon(face_landmark['top_lip'],fill=(150,0,0,120))
            draw.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 130))

            draw.line(face_landmark['top_lip'],fill=(150,0,0,70),width=2)
            draw.line(face_landmark['bottom_lip'], fill=(150, 0, 0, 70),width=2)
            #绘制左右眼睛
            draw.polygon(face_landmark['left_eye'],fill=(255,255,255,20))
            draw.polygon(face_landmark['right_eye'],fill=(255,255,255,20))
            draw.line(face_landmark['left_eye']+[face_landmark['left_eye'][0]], fill=(0, 0, 0, 20))
            draw.line(face_landmark['right_eye']+[face_landmark['right_eye'][0]], fill=(0, 0, 0, 20))


        # pil_image.show()
        filename = self.save_pil_face(pil_image)
        return [filename]
    # 5.人脸68个特侦点获取
    def face_68_piont(self):
        #读取图片
        image = cv2.imread(os.path.join(self.dir_path,self.pic_name))
        #使用特征提取器
        detector = dlib.get_frontal_face_detector()
        #定义模型的路径
        model_path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            'static/model/shape_predictor_68_face_landmarks.dat'
        )
        #定义预测器
        predictor = dlib.shape_predictor(model_path)
        #实例化特侦提取器
        dets = detector(image,1)
        for k,d in enumerate(dets):
            #利用预测器预测
            shape = predictor(image,d)
            #标出68个点
            for i in range(68):
                #画原点，圆心
                cv2.circle(
                    image,
                    (shape.part(i).x,shape.part(i).y),
                    1,
                    (255,0,0),
                    -1
                )
                #标记为每一个点标记序号
                # cv2.putText(
                #     image,
                #     str(i),
                #     (shape.part(i).x,shape.part(i).y),
                #     cv2.FONT_HERSHEY_COMPLEX,
                #     0.3,
                #     (0, 0, 255),
                # )
        # cv2.imshow("face_68_predict.png",image)
        # cv2.waitKey(0)
        filename = self.save_cv2_face(image)
        return [filename]
    #使用opencv保存图片
    def save_cv2_face(self,image):
        #如果保存目录不存在就创建
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        #定义图片完整名称
        filename = "{}.png".format(
            self.image_name
        )
        #保存图片到指定的位子
        cv2.imwrite(os.path.join(
            self.save_path,
            filename),
            image

        )
        return filename

if __name__ == "__main__":

    root_path = os.path.dirname(
        os.path.dirname(__file__)
    )
    face = Face(
        directory_path=os.path.join(root_path,'static/images/'),
        picture_name='face_group.jpg',
        save_path=os.path.join(root_path,'static/uploads')
    )
    image,face_locations = face.get_face_location()
    print(face_locations)
    print(face.face_box())
    print(face.face_sense())
    print(face.face_find())
    face.face_makeup()

    # print(face.face_makeup())
    face.face_68_piont()
