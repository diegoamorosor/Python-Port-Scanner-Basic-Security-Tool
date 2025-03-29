import socket
import sys
import datetime
import argparse
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, target, start_port=1, end_port=1024, timeout=1):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout
        self.open_ports = []

    def scan_port(self, port):
        """Escanea un puerto específico"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)

        try:
            result = sock.connect_ex((self.target, port))
            if result == 0:
                service = self.get_service_name(port)
                self.open_ports.append((port, service))
            sock.close()

        except socket.error:
            pass

    def get_service_name(self, port):
        """Obtiene el nombre del servicio para un puerto conocido"""
        try:
            service = socket.getservbyport(port)
            return service
        except:
            return "unknown"

    def run_scan(self):
        """Ejecuta el escaneo de puertos usando múltiples hilos"""
        print(f"\nIniciando escaneo de {self.target}")
        print(f"Tiempo de inicio: {datetime.datetime.now()}\n")

        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(self.scan_port, range(self.start_port, self.end_port + 1))

        return self.generate_report()

    def generate_report(self):
        """Genera un reporte del escaneo"""
        report = []
        report.append("=" * 50)
        report.append(f"Reporte de escaneo para: {self.target}")
        report.append(f"Fecha y hora: {datetime.datetime.now()}")
        report.append("=" * 50)

        if self.open_ports:
            report.append("\nPuertos abiertos encontrados:")
            report.append("-" * 30)
            for port, service in sorted(self.open_ports):
                report.append(f"Puerto {port}: {service}")
        else:
            report.append("\nNo se encontraron puertos abiertos en el rango especificado.")

        report.append("\n" + "=" * 50)
        return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description='Scanner de puertos básico para seguridad')
    parser.add_argument('target', help='Dirección IP o hostname objetivo')
    parser.add_argument('-s', '--start', type=int, default=1, help='Puerto inicial (default: 1)')
    parser.add_argument('-e', '--end', type=int, default=1024, help='Puerto final (default: 1024)')
    parser.add_argument('-t', '--timeout', type=float, default=1, help='Timeout en segundos (default: 1)')

    args = parser.parse_args()

    try:
        scanner = PortScanner(
            args.target,
            start_port=args.start,
            end_port=args.end,
            timeout=args.timeout
        )
        report = scanner.run_scan()
        print(report)

    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
        sys.exit(1)
    except socket.gaierror:
        print("\nError: No se puede resolver el hostname.")
        sys.exit(1)

if __name__ == "__main__":
    main()