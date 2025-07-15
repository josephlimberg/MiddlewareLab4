from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import mysql.connector

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        try:
            conn = mysql.connector.connect(
                host="000.000.000.000",
                port=3306,
                user="admin",
                password="admin",
                database="saludosdb"
            )
            cursor = conn.cursor()

            args = [request.name, ""]
            result = cursor.callproc("GetSaludo", args)

            saludo = result[1]

            cursor.close()
            conn.close()

            return helloworld_pb2.HelloReply(message=saludo)

        except Exception as e:
            return helloworld_pb2.HelloReply(message=f"Error en servidor: {str(e)}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('0.0.0.0:50051')
    print("Servidor escuchando en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
