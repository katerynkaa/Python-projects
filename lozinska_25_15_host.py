
import socketserver
import random


class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self):

        print('connected from', self.client_address)

        send = bytes('Start test? y/n', encoding='utf-8')
        self.wfile.write(send + b'\n')
        answer1 = self.rfile.readline().strip()
        answer = str(answer1, encoding='utf-8')

        while True:
            if answer=='y':
                points = self.q_reader()
                self.wfile.write(bytes('you have recieved ' + str(points) + ' points', encoding='utf-8')+ b'\n')
                break
            elif answer=='n':
                self.wfile.write(bytes('Goodbye',encoding='utf-8')+ b'\n')
                break
            else:
                self.wfile.write(bytes('Wrong input',encoding='utf-8')+ b'\n')

    def q_reader(self):

        with open('questions.txt') as questions_file:
            all_questions = questions_file.readlines()

            point = 0
            ch = [] #перемішаний список питань
            self.q_chooser(all_questions, ch)
            for j in range(len(all_questions)//5):
                q =ch[j]
                to_send = str(all_questions[q][0:-1] + '  ' + all_questions[q+1][0:-1] +'  ' + all_questions[q+2][0:-1] +'  ' + all_questions[q+3][0:-1])
                #print(to_send)
                self.wfile.write(bytes(to_send, encoding='utf-8')+ b'\n')

                p_answer = self.rfile.readline().strip()
                answer = str(p_answer, encoding='utf-8')
                if answer +  '\n' == all_questions[q+4] or answer == all_questions[q+4]:
                    point += 1
                else:
                    point += 0
            return point

    def q_chooser(self, all_questions, ch): #створює список питань
        n = []
        j = 0
        for i in range(len(all_questions) // 5):
            n.append(j)
            j += 5
        self.n_chooser(n, ch, all_questions)

    def n_chooser(self,n ,ch, all_questions): #перемішує питання
        while len(ch)!= len(all_questions)//5:
            nn = random.randint(0, len(all_questions)-1)
            if ch.count(nn)==0 and nn in n:
                ch.append(nn)






if __name__ == '__main__':
    print('=== quiz server ===')
    socketserver.TCPServer(('',1401), RequestHandler).serve_forever() 