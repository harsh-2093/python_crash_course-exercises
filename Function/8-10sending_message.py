def print_message(message,message_sent):
    while message:
        current_message=message.pop()
        print(f"current messsage:{current_message}")
        message_sent.append(current_message)
        
    
message=["hi abhram","hi colie","did u rech home","how was ur experience","di u loose?"]
message_sent=[]

print_message(message,message_sent)
print(list(reversed(message_sent)))

