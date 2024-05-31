import tkinter as tk
import boto3

# get data from aws
ec2 = boto3.client('ec2')
response = ec2.describe_instances()

root = tk.Tk()

# add label
message = tk.Label(root, text=response)
message.pack()

root.mainloop()
