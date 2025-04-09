import sys
import logging
#exc_tb - on which file exception has occured and which line execption has occured

def error_message_detail(error,error_detail:sys): #error_detail is present inside sys
    _,_,exc_tb= error_detail.exc_info() #this will give us 3 execution info and we are intrstd only in last info thats exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)) #tb_lineno gives us the line number where error has occured 
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)  #this will call the error_message_detail function and will give us the error message in a formatted way

    def __str__(self):
        return self.error_message
    
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e,sys) 
