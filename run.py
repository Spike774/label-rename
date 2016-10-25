# -*- coding: UTF-8 -*-

import os


path = 'C:\\x-Exchang space\\google-static-sat-image-load\\image_cache\\Sample\\pos\\needrename'

i = 1405

count = 1
sum_f = len(os.listdir(path))

for f in os.listdir(path):

    if f.endswith('.png'):
        modi_name = 'pos_{0}.png'.format(i)
        os.rename(os.path.join(path, f), os.path.join(path, modi_name))
        print '... {0}/{1} ...'.format(count, sum_f)
        i += 1
        count += 1

print 'complete'