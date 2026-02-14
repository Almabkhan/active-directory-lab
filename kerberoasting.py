#!/usr/bin/env python3
"""
Kerberoasting Simulation - Educational
"""

class KerberoastingSim:
    def __init__(self):
        self.accounts = [
            {'name': 'sql_svc', 'password': 'P@ssw0rd123'},
            {'name': 'web_svc', 'password': 'Summer2024!'}
        ]
    
    def demonstrate(self):
        print("="*50)
        print("KERBEROASTING SIMULATION")
        print("="*50)
        
        print("\n[+] SPNs found:")
        for acc in self.accounts:
            print(f"  • {acc['name']}")
        
        print("\n[+] Weak passwords found:")
        for acc in self.accounts:
            print(f"  • {acc['name']}: {acc['password']}")

def main():
    sim = KerberoastingSim()
    sim.demonstrate()

if __name__ == "__main__":
    main()