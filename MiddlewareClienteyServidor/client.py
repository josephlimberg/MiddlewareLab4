import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
       
    nombre = input("Ingresa tu nombre: ")
    response = stub.SayHello(helloworld_pb2.HelloRequest(name=nombre))
    print("Respuesta del servidor:", response.message)

if __name__ == '__main__':
    run()

