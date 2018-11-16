import tensorflow as tf

train = True

class CycleGAN():
    def setup_input(self):
        
        filenames_A = tf.train.match_filenames_once("./input/horse2zebra/trainA/*.jpg")
        self.queue_length_A = tf.size(filenames_A)

        filenames_B = tf.train.match_filenames_once("./input/horse2zebra/trainB/*.jpg")
        self.queue_length_B = tf.size(filenames_B)
        
        filename_queue_A = tf.data.Dataset.from_tensor_slices(filenames_A)
        filename_queue_B = tf.data.Dataset.from_tensor_slices(filenames_B)

        # image_reader = tf.WholeFileReader()
        # _, image_file_A = image_reader.read(filename_queue_A)
        # _, image_file_B = image_reader.read(filename_queue_B)

        # self.image_A = tf.subtract(tf.div(tf.image.resize_images(tf.image.decode_jpeg(image_file_A),[256,256]),127.5),1)
        # self.image_B = tf.subtract(tf.div(tf.image.resize_images(tf.image.decode_jpeg(image_file_B),[256,256]),127.5),1)

        with tf.Session() as session:
            init = (tf.global_variables_initializer(), tf.local_variables_initializer())
            session.run(init)
            for pair in filename_queue_A:
                print(pair)
            #print(session.run(filename_queue_A))

    def setup_model(self):
        pass

    def setup_loss(self):
        pass
    
    def read_input(self):
        pass

    def train(self):
        self.setup_input()
        #self.setup_model()
        #self.setup_loss()

        #init = (tf.global_variables_initializer(), tf.local_variables_initializer())
        #saver = tf.train.Saver()

        #with tf.Session() as session:
            #pass

    def test(self):
        pass

if __name__ == '__main__':
    model = CycleGAN()
    if train:
        model.train()
    else:
        model.test()