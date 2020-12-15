import pickle
import sys
import os

""" if sys.argv[1].lower() == 'initialize':
    # Initialize image counter. 
    with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','wb') as f:
        pickle.dump(0,f)

    # Initialize last duty cycle value.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','wb') as f:
        pickle.dump(2,f)

if sys.argv[1].lower() == 'erase':
    with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','wb') as f:
        pickle.dump(0,f)
        os.system('rm -rf /home/pi/Sync/*.jpg')

if sys.argv[1].lower() == 'reset':
    with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','wb') as f:
        pickle.dump(0,f)
        os.system('rm -rf /home/pi/Sync/*.jpg')

    with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','wb') as f:
        pickle.dump(2,f) """

with open(os.path.dirname(os.path.abspath(__file__)) + '/counter','wb') as f:
    pickle.dump(0,f)
    os.system('rm -rf /home/pi/Sync/*.jpg')

with open(os.path.dirname(os.path.abspath(__file__)) + '/ldc','wb') as f:
    pickle.dump(2,f) 
    
