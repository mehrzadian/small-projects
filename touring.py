class delta:
    def __init__(self,currentState, nextState, currentChar, nextChar, dir):
        self.currentState=currentState
        self.nextState=nextState
        self.currentChar=currentChar
        self.nextChar=nextChar
        self.dir=dir
    def isMatch(self,currentState,currentChar):
        return self.currentState==currentState and self.currentChar==currentChar


class Turing:
    def __init__(self, tape, delta, startState, acceptState):
        self.tape=tape
        self.delta=delta
        self.startState=startState
        self.acceptState=acceptState
        
        self.currentState=startState
        self.head=1
    def run(self):
        self.tape+='B'
        self.tape=['B']+self.tape
        while self.currentState!=self.acceptState and self.head!=len(self.tape):
            
            currentChar=self.tape[self.head]
            for i,d in enumerate(self.delta):
                if d.isMatch(self.currentState,currentChar)==False and i==len(self.delta)-1:
                    return 'halt'
                if d.isMatch(self.currentState,currentChar):
                    self.currentState=d.nextState
                    self.tape[self.head]=d.nextChar
                    if d.dir=='L':
                        self.head-=1
                    elif d.dir=='R':
                        self.head+=1
                    break
                
            
        return self.currentState==self.acceptState
#test case
tape="aaabbb"
delta=[delta('q0','q1','a','x','R'), delta('q1','q1','a','a','R'),
       delta('q1','q2','b','y','L'), delta('q2','q2','y','y','L'),
       delta('q2','q2','a','a','L'), delta('q2','q0','x','x','R'),
       delta('q0','q3','y','y','R'), delta('q3','q3','y','y','R'),
       delta('q3','q4','B','B',"R"), delta('q1','q1','y','y','R')]
startState='q0'
acceptState='q4'

turing=Turing(list(tape),delta,startState,acceptState)
print(turing.run())

tape2  = 'aabbbb'
turing=Turing(list(tape2),delta,startState,acceptState)
print(turing.run())
