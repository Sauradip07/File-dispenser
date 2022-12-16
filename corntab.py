from corntab import CornTab
corn = CornTab(user="sauradip")
job = corn.new(command = 'python file-dispenser.py')
job.minute.every(1)
corn.write()