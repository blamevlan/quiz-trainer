#!/usr/bin/env python3
# IT Quiz Trainer für FiSis
# github.com/blamevlan

import random
import os

GRN = "\033[92m"; RED = "\033[91m"; YLW = "\033[93m"
BLU = "\033[94m"; CYN = "\033[96m"; MGN = "\033[95m"
BLD = "\033[1m";  DIM = "\033[2m";  RST = "\033[0m"

LETTERS = ["1", "2", "3", "4"]

# ── Sprachen ───────────────────────────────────────────────────────────────────
LANG = {
    "de": {
        "subtitle":     "IT Quiz Trainer für FiSis  github.com/blamevlan",
        "lang_prompt":  "Sprache / Language (de/en)",
        "menu_title":   "Was möchtest du üben?",
        "mode1":        "OSI-Schichten  — Protokolle, Geräte, Funktionen zuordnen",
        "mode2":        "Abkürzungen    — IT-Begriffe kennen und erklären",
        "mode3":        "IT-Sicherheit  — CIA-Triad, BSI, Konzepte, Ports",
        "mode_prompt":  "Auswahl (1/2/3)",
        "diff_title":   "Schwierigkeit:",
        "diff1":        "Basics    — Grundlagen und häufige Prüfungsthemen",
        "diff2":        "Erweitert — alle Fragen inkl. Spezialwissen",
        "diff_prompt":  "Auswahl (1/2)",
        "correct":      "✓ Richtig!",
        "wrong":        "✗ Falsch.",
        "correct_ans":  "Richtige Antwort",
        "tip_label":    "Erklärung",
        "continue":     "Weiter? (Enter = ja, m = Menü, q = Beenden)",
        "result":       "Ergebnis:",
        "right_count":  "Richtig",
        "wrong_count":  "Falsch",
        "total":        "Gesamt",
        "score_good":   "Gut gemacht! Du bist bereit für die Prüfung!",
        "score_mid":    "Nicht schlecht — weiter üben!",
        "score_bad":    "Nochmal von vorne — du schaffst das!",
        "back_hint":    "m = zurück zum Menü",
        "input_hint":   "m=Menü, q=Beenden",
        "mc_prompt":    "Auswahl (1/2/3/4)",
        "your_ans":     "Deine Antwort",
        "try_again":    "Nochmal — kein Hinweis diesmal.",
        "hint_now":     "Hinweis",
        "last_try":     "Letzter Versuch",
        "attempt":      "Versuch",
        "quit_label":   "Beenden",
        "or_label":     "oder",
        "round_label":  "Frage",
        "all_done":     "Alle Fragen beantwortet!",
        "questions": {
            "osi": [
                # ── BASICS ──
                {
                    "q": "Auf welcher OSI-Schicht arbeitet das IP-Protokoll?",
                    "opts": ["Schicht 3 — Vermittlung (Network)", "Schicht 2 — Sicherung (Data Link)", "Schicht 4 — Transport", "Schicht 1 — Bitübertragung (Physical)"],
                    "tip": "IP ist ein Layer-3-Protokoll. Router arbeiten auf Schicht 3.",
                    "level": "easy"
                },
                {
                    "q": "Wie heißt OSI-Schicht 7?",
                    "opts": ["Anwendungsschicht (Application)", "Sitzungsschicht (Session)", "Transportschicht (Transport)", "Darstellungsschicht (Presentation)"],
                    "tip": "Schicht 7 ist die Anwendungsschicht. HTTP, FTP, DNS und SMTP arbeiten hier.",
                    "level": "easy"
                },
                {
                    "q": "Wie heißt OSI-Schicht 1?",
                    "opts": ["Bitübertragungsschicht (Physical)", "Sicherungsschicht (Data Link)", "Vermittlungsschicht (Network)", "Transportschicht (Transport)"],
                    "tip": "Schicht 1 überträgt rohe Bits über ein physisches Medium. Kabel, Hubs, Repeater.",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet ein Switch?",
                    "opts": ["Schicht 2 — Sicherung (Data Link)", "Schicht 1 — Bitübertragung (Physical)", "Schicht 3 — Vermittlung (Network)", "Schicht 4 — Transport"],
                    "tip": "Ein Switch arbeitet mit MAC-Adressen auf Schicht 2. Layer-3-Switches können auch routen.",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet ein Router?",
                    "opts": ["Schicht 3 — Vermittlung (Network)", "Schicht 2 — Sicherung (Data Link)", "Schicht 4 — Transport", "Schicht 7 — Anwendung (Application)"],
                    "tip": "Router vermitteln Pakete anhand von IP-Adressen — das ist Schicht 3.",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet TCP?",
                    "opts": ["Schicht 4 — Transport", "Schicht 3 — Vermittlung (Network)", "Schicht 2 — Sicherung (Data Link)", "Schicht 7 — Anwendung (Application)"],
                    "tip": "TCP und UDP sind Transportprotokolle — Schicht 4.",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet HTTP?",
                    "opts": ["Schicht 7 — Anwendung (Application)", "Schicht 4 — Transport", "Schicht 3 — Vermittlung (Network)", "Schicht 6 — Darstellung (Presentation)"],
                    "tip": "HTTP ist ein Anwendungsprotokoll — Schicht 7.",
                    "level": "easy"
                },
                {
                    "q": "Wie heißt OSI-Schicht 2?",
                    "opts": ["Sicherungsschicht (Data Link)", "Bitübertragungsschicht (Physical)", "Vermittlungsschicht (Network)", "Transportschicht (Transport)"],
                    "tip": "Schicht 2 sichert die Übertragung zwischen direkt verbundenen Geräten. MAC-Adressen, Ethernet.",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet ein Hub?",
                    "opts": ["Schicht 1 — Bitübertragung (Physical)", "Schicht 2 — Sicherung (Data Link)", "Schicht 3 — Vermittlung (Network)", "Schicht 4 — Transport"],
                    "tip": "Ein Hub leitet alle Signale an alle Ports weiter — rein physisch, Schicht 1.",
                    "level": "easy"
                },
                {
                    "q": "Wie heißt OSI-Schicht 4?",
                    "opts": ["Transportschicht (Transport)", "Sitzungsschicht (Session)", "Vermittlungsschicht (Network)", "Anwendungsschicht (Application)"],
                    "tip": "Schicht 4 regelt den zuverlässigen Transport von Daten. TCP und UDP.",
                    "level": "easy"
                },
                {
                    "q": "Welche Schicht ist für MAC-Adressen zuständig?",
                    "opts": ["Schicht 2 — Sicherung (Data Link)", "Schicht 3 — Vermittlung (Network)", "Schicht 1 — Bitübertragung (Physical)", "Schicht 4 — Transport"],
                    "tip": "MAC-Adressen sind Hardware-Adressen und gehören zur Sicherungsschicht (Schicht 2).",
                    "level": "easy"
                },
                {
                    "q": "Auf welcher Schicht arbeitet UDP?",
                    "opts": ["Schicht 4 — Transport", "Schicht 3 — Vermittlung (Network)", "Schicht 7 — Anwendung (Application)", "Schicht 2 — Sicherung (Data Link)"],
                    "tip": "UDP ist wie TCP ein Transportprotokoll — Schicht 4. Schnell, ohne Verbindungsaufbau.",
                    "level": "easy"
                },
                # ── ERWEITERT ──
                {
                    "q": "Auf welcher OSI-Schicht arbeitet SSL/TLS?",
                    "opts": ["Schicht 6 — Darstellung (Presentation)", "Schicht 4 — Transport", "Schicht 7 — Anwendung (Application)", "Schicht 5 — Sitzung (Session)"],
                    "tip": "SSL/TLS verschlüsselt und kodiert Daten — das ist Aufgabe der Darstellungsschicht (Schicht 6).",
                    "level": "hard"
                },
                {
                    "q": "Wie heißt OSI-Schicht 5?",
                    "opts": ["Sitzungsschicht (Session)", "Darstellungsschicht (Presentation)", "Transportschicht (Transport)", "Anwendungsschicht (Application)"],
                    "tip": "Schicht 5 baut Sitzungen auf, verwaltet und beendet sie. NetBIOS, RPC.",
                    "level": "hard"
                },
                {
                    "q": "Wie heißt OSI-Schicht 6?",
                    "opts": ["Darstellungsschicht (Presentation)", "Sitzungsschicht (Session)", "Anwendungsschicht (Application)", "Transportschicht (Transport)"],
                    "tip": "Schicht 6 wandelt Daten in ein einheitliches Format um. Verschlüsselung, Komprimierung, Zeichensätze.",
                    "level": "hard"
                },
                {
                    "q": "Was ist die Hauptaufgabe der Sitzungsschicht (Schicht 5)?",
                    "opts": ["Aufbau, Verwaltung und Abbau von Kommunikationssitzungen", "Datenverschlüsselung und Komprimierung", "Weiterleitung von Paketen anhand von IP-Adressen", "Fehlererkennung bei der Datenübertragung"],
                    "tip": "Schicht 5 koordiniert den Dialog zwischen zwei Systemen — Aufbau, Synchronisation, Abbau.",
                    "level": "hard"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet DNS?",
                    "opts": ["Schicht 7 — Anwendung (Application)", "Schicht 3 — Vermittlung (Network)", "Schicht 4 — Transport", "Schicht 5 — Sitzung (Session)"],
                    "tip": "DNS ist ein Anwendungsprotokoll — Schicht 7.",
                    "level": "hard"
                },
                {
                    "q": "Auf welcher OSI-Schicht arbeitet SMTP?",
                    "opts": ["Schicht 7 — Anwendung (Application)", "Schicht 4 — Transport", "Schicht 6 — Darstellung (Presentation)", "Schicht 3 — Vermittlung (Network)"],
                    "tip": "SMTP überträgt E-Mails — es ist ein Anwendungsprotokoll auf Schicht 7.",
                    "level": "hard"
                },
                {
                    "q": "Was macht die Darstellungsschicht (Schicht 6)?",
                    "opts": ["Datenkodierung, Verschlüsselung und Komprimierung", "Aufbau und Abbau von Verbindungen", "Weiterleitung von Datenpaketen", "Zuverlässige Ende-zu-Ende-Übertragung"],
                    "tip": "Schicht 6 stellt sicher, dass Daten in einem für den Empfänger lesbaren Format vorliegen.",
                    "level": "hard"
                },
                {
                    "q": "Auf welcher Schicht arbeitet FTP?",
                    "opts": ["Schicht 7 — Anwendung (Application)", "Schicht 4 — Transport", "Schicht 3 — Vermittlung (Network)", "Schicht 6 — Darstellung (Presentation)"],
                    "tip": "FTP ist ein Anwendungsprotokoll — Schicht 7.",
                    "level": "hard"
                },
            ],
            "abk": [
                # ── BASICS ──
                {"q": "Wofür steht DNS?", "opts": ["Domain Name System", "Dynamic Network Service", "Data Name Server", "Domain Node System"], "tip": "DNS löst Hostnamen in IP-Adressen auf.", "level": "easy"},
                {"q": "Wofür steht DHCP?", "opts": ["Dynamic Host Configuration Protocol", "Domain Host Control Protocol", "Dynamic Hardware Configuration Protocol", "Data Host Communication Protocol"], "tip": "DHCP vergibt automatisch IP-Adressen, Subnetzmaske, Gateway und DNS an Clients.", "level": "easy"},
                {"q": "Wofür steht HTTP?", "opts": ["Hypertext Transfer Protocol", "High Transfer Text Protocol", "Hypertext Transmission Program", "Host Transfer Text Protocol"], "tip": "HTTP ist das Protokoll für Webseiten. Port 80.", "level": "easy"},
                {"q": "Wofür steht HTTPS?", "opts": ["Hypertext Transfer Protocol Secure", "High Transfer Text Protocol Secure", "Hypertext Transmission Protocol System", "Host Transfer Text Protocol Secure"], "tip": "HTTPS ist HTTP mit TLS-Verschlüsselung. Port 443.", "level": "easy"},
                {"q": "Wofür steht TCP?", "opts": ["Transmission Control Protocol", "Transfer Communication Protocol", "Transport Control Program", "Terminal Connection Protocol"], "tip": "TCP sorgt für zuverlässige, geordnete Übertragung mit Fehlerkorrektur.", "level": "easy"},
                {"q": "Wofür steht UDP?", "opts": ["User Datagram Protocol", "Universal Data Protocol", "Unified Datagram Program", "User Data Program"], "tip": "UDP überträgt schnell ohne Verbindungsaufbau — ohne Garantie. Streaming, DNS, VoIP.", "level": "easy"},
                {"q": "Wofür steht VPN?", "opts": ["Virtual Private Network", "Virtual Protocol Network", "Verified Private Network", "Virtual Public Network"], "tip": "Ein VPN verschlüsselt den Datenverkehr und verbindet Netzwerke sicher über das Internet.", "level": "easy"},
                {"q": "Wofür steht LAN?", "opts": ["Local Area Network", "Long Area Network", "Local Access Node", "Linked Area Network"], "tip": "LAN bezeichnet ein lokales Netzwerk, z.B. in einem Büro oder Gebäude.", "level": "easy"},
                {"q": "Wofür steht WAN?", "opts": ["Wide Area Network", "Wireless Area Network", "Wide Access Node", "World Area Network"], "tip": "WAN verbindet Netzwerke über große geografische Distanzen. Das Internet ist das größte WAN.", "level": "easy"},
                {"q": "Wofür steht SSH?", "opts": ["Secure Shell", "System Shell Handler", "Secure Socket Host", "System Secure Host"], "tip": "SSH ermöglicht sichere, verschlüsselte Fernzugriffe. Port 22.", "level": "easy"},
                {"q": "Wofür steht FTP?", "opts": ["File Transfer Protocol", "Fast Transfer Protocol", "File Transmission Program", "Full Transfer Protocol"], "tip": "FTP überträgt Dateien. Port 21 (Steuerung), 20 (Daten). Unverschlüsselt — lieber SFTP.", "level": "easy"},
                {"q": "Wofür steht NAT?", "opts": ["Network Address Translation", "Network Access Technology", "Node Address Transfer", "Network Allocation Table"], "tip": "NAT übersetzt private IP-Adressen in öffentliche — viele Geräte teilen eine öffentliche IP.", "level": "easy"},
                {"q": "Wofür steht MAC (Netzwerk)?", "opts": ["Media Access Control", "Machine Access Code", "Media Address Code", "Main Access Control"], "tip": "Die MAC-Adresse ist eine Hardware-Adresse, weltweit eindeutig (48 Bit).", "level": "easy"},
                {"q": "Wofür steht WLAN?", "opts": ["Wireless Local Area Network", "Wide Local Area Network", "Wireless Linked Access Node", "Wide Linked Area Network"], "tip": "WLAN ist das Funknetzwerk nach IEEE 802.11. Umgangssprachlich Wi-Fi.", "level": "easy"},
                {"q": "Wofür steht IP?", "opts": ["Internet Protocol", "Internal Protocol", "Interface Program", "Internet Program"], "tip": "IP adressiert Geräte und leitet Pakete. IPv4 (32 Bit), IPv6 (128 Bit).", "level": "easy"},
                # ── ERWEITERT ──
                {"q": "Wofür steht OSPF?", "opts": ["Open Shortest Path First", "Open System Path Finder", "Optimized Shortest Path Forward", "Open Subnet Path First"], "tip": "OSPF ist ein Link-State-Routing-Protokoll für interne Netzwerke (IGP).", "level": "hard"},
                {"q": "Wofür steht BGP?", "opts": ["Border Gateway Protocol", "Basic Gateway Protocol", "Border Group Protocol", "Broadband Gateway Protocol"], "tip": "BGP ist das Routing-Protokoll des Internets — verbindet autonome Systeme (AS).", "level": "hard"},
                {"q": "Wofür steht ICMP?", "opts": ["Internet Control Message Protocol", "Internal Control Message Protocol", "Internet Communication Management Protocol", "Integrated Control Message Protocol"], "tip": "ICMP meldet Netzwerkfehler. Wird von ping und traceroute genutzt.", "level": "hard"},
                {"q": "Wofür steht ARP?", "opts": ["Address Resolution Protocol", "Automatic Routing Protocol", "Address Routing Program", "Access Resolution Protocol"], "tip": "ARP löst IP-Adressen in MAC-Adressen auf — im lokalen Netzwerk.", "level": "hard"},
                {"q": "Wofür steht LDAP?", "opts": ["Lightweight Directory Access Protocol", "Local Directory Access Protocol", "Linked Data Access Protocol", "Lightweight Data Application Protocol"], "tip": "LDAP fragt Verzeichnisdienste ab. Active Directory basiert auf LDAP.", "level": "hard"},
                {"q": "Wofür steht PKI?", "opts": ["Public Key Infrastructure", "Private Key Interface", "Public Key Interface", "Protocol Key Infrastructure"], "tip": "PKI verwaltet digitale Zertifikate und öffentliche Schlüssel.", "level": "hard"},
                {"q": "Wofür steht MFA?", "opts": ["Multi-Factor Authentication", "Multi-Frequency Access", "Managed Factor Authentication", "Multi-Function Application"], "tip": "MFA verlangt mindestens zwei Faktoren: Wissen (PIN), Besitz (Token), Biometrie.", "level": "hard"},
                {"q": "Wofür steht CVSS?", "opts": ["Common Vulnerability Scoring System", "Central Vulnerability Security System", "Common Vulnerability Security Score", "Centralized Vulnerability Scoring System"], "tip": "CVSS bewertet Schwachstellen auf einer Skala von 0 bis 10.", "level": "hard"},
                {"q": "Wofür steht IDS?", "opts": ["Intrusion Detection System", "Internal Defense System", "Integrated Detection System", "Intrusion Defense System"], "tip": "Ein IDS erkennt Angriffe und meldet sie — blockiert aber nicht aktiv.", "level": "hard"},
                {"q": "Wofür steht IPS?", "opts": ["Intrusion Prevention System", "Internal Protection System", "Integrated Prevention System", "Intrusion Protection Service"], "tip": "Ein IPS erkennt Angriffe und blockiert sie aktiv — Weiterentwicklung des IDS.", "level": "hard"},
                {"q": "Wofür steht VLAN?", "opts": ["Virtual Local Area Network", "Very Local Area Network", "Virtual Linked Access Network", "Variable Local Area Network"], "tip": "VLANs segmentieren ein physisches Netz in logische Teilnetze auf Layer 2.", "level": "hard"},
                {"q": "Wofür steht CIDR?", "opts": ["Classless Inter-Domain Routing", "Central Internet Domain Routing", "Common Inter-Domain Routing", "Classless Internet Domain Registry"], "tip": "CIDR ersetzt die Klassen A/B/C und ermöglicht flexible Subnetzmasken.", "level": "hard"},
                {"q": "Wofür steht SMTP?", "opts": ["Simple Mail Transfer Protocol", "Secure Mail Transfer Protocol", "Standard Mail Transfer Protocol", "Simple Message Transfer Program"], "tip": "SMTP sendet E-Mails. Port 25 (Server–Server), 587 (Client–Server, verschlüsselt).", "level": "hard"},
                {"q": "Wofür steht IMAP?", "opts": ["Internet Message Access Protocol", "Internal Mail Access Protocol", "Internet Mail Application Protocol", "Integrated Message Access Protocol"], "tip": "IMAP lädt E-Mails vom Server und synchronisiert sie. Port 143, verschlüsselt 993.", "level": "hard"},
                {"q": "Wofür steht RAID?", "opts": ["Redundant Array of Independent Disks", "Rapid Array of Internal Disks", "Redundant Access of Independent Drives", "Remote Array of Integrated Disks"], "tip": "RAID kombiniert mehrere Festplatten für Ausfallsicherheit oder Performance.", "level": "hard"},
                {"q": "Wofür steht SLA?", "opts": ["Service Level Agreement", "System Level Agreement", "Service Linked Application", "Standard Level Agreement"], "tip": "Ein SLA definiert zugesicherte Leistungsmerkmale wie Verfügbarkeit oder Reaktionszeiten.", "level": "hard"},
            ],
            "itg": [
                # ── BASICS ──
                {
                    "q": "Wofür stehen die drei Buchstaben der CIA-Triad?",
                    "opts": ["Confidentiality, Integrity, Availability", "Control, Integrity, Access", "Confidentiality, Integration, Authorization", "Control, Integration, Availability"],
                    "tip": "CIA = Vertraulichkeit, Integrität, Verfügbarkeit — die drei Grundziele der IT-Sicherheit.",
                    "level": "easy"
                },
                {
                    "q": "Was bedeutet Vertraulichkeit (Confidentiality)?",
                    "opts": ["Nur Berechtigte können auf Daten zugreifen", "Daten sind vollständig und unverändert", "Systeme sind für Berechtigte nutzbar", "Jede Aktion ist nachvollziehbar"],
                    "tip": "Vertraulichkeit schützt Daten vor unbefugtem Zugriff, z.B. durch Verschlüsselung.",
                    "level": "easy"
                },
                {
                    "q": "Was bedeutet Integrität (Integrity)?",
                    "opts": ["Daten sind vollständig und unverändert", "Nur Berechtigte können auf Daten zugreifen", "Systeme sind für Berechtigte nutzbar", "Änderungen sind nachvollziehbar"],
                    "tip": "Integrität stellt sicher, dass Daten nicht unbemerkt verändert wurden, z.B. durch Hashes.",
                    "level": "easy"
                },
                {
                    "q": "Was bedeutet Verfügbarkeit (Availability)?",
                    "opts": ["Systeme und Daten sind für Berechtigte nutzbar wenn sie gebraucht werden", "Daten sind verschlüsselt und geschützt", "Änderungen werden protokolliert", "Nur Berechtigte können Daten verändern"],
                    "tip": "Verfügbarkeit bedeutet: kein Ausfall, kein Denial of Service. Systeme müssen erreichbar sein.",
                    "level": "easy"
                },
                {
                    "q": "Wofür steht BSI in Deutschland?",
                    "opts": ["Bundesamt für Sicherheit in der Informationstechnik", "Bundesstelle für Systemintegration", "Behörde für Sicherheit und Infrastruktur", "Bundesamt für Systemsicherheit und IT"],
                    "tip": "Das BSI ist die nationale Cybersicherheitsbehörde Deutschlands.",
                    "level": "easy"
                },
                {
                    "q": "Was ist der Unterschied zwischen Authentifizierung und Autorisierung?",
                    "opts": ["Authentifizierung prüft die Identität, Autorisierung vergibt Rechte", "Autorisierung prüft die Identität, Authentifizierung vergibt Rechte", "Beide prüfen die Identität des Benutzers", "Autorisierung verschlüsselt den Zugriff"],
                    "tip": "Erst authentifizieren (Wer bist du?), dann autorisieren (Was darfst du?).",
                    "level": "easy"
                },
                {
                    "q": "Welchen Port verwendet HTTPS?",
                    "opts": ["443", "80", "8080", "8443"],
                    "tip": "HTTP nutzt Port 80, HTTPS Port 443.",
                    "level": "easy"
                },
                {
                    "q": "Welchen Port verwendet SSH?",
                    "opts": ["22", "23", "21", "3389"],
                    "tip": "SSH nutzt Port 22. Telnet (unsicher) nutzt Port 23.",
                    "level": "easy"
                },
                {
                    "q": "Was ist eine Schwachstelle (Vulnerability)?",
                    "opts": ["Eine Schwäche in einem System, die ausgenutzt werden kann", "Ein aktiver Angriff auf ein System", "Ein Sicherheitspatch", "Ein Eindringling im Netzwerk"],
                    "tip": "Vulnerability = Schwachstelle. Threat = Bedrohung. Risk = Wahrscheinlichkeit × Auswirkung.",
                    "level": "easy"
                },
                {
                    "q": "Was ist ein Backup?",
                    "opts": ["Eine gesicherte Kopie von Daten zur Wiederherstellung", "Eine Verschlüsselung von Daten", "Ein Protokoll zur Datenübertragung", "Eine Methode zur Zugangskontrolle"],
                    "tip": "Backups schützen vor Datenverlust durch Ransomware, Hardware-Ausfall oder menschliche Fehler.",
                    "level": "easy"
                },
                # ── ERWEITERT ──
                {
                    "q": "Was ist der Unterschied zwischen IDS und IPS?",
                    "opts": ["IDS erkennt Angriffe und meldet sie, IPS erkennt und blockiert aktiv", "IPS erkennt Angriffe und meldet sie, IDS blockiert aktiv", "IDS ist für Netzwerke, IPS für Hosts", "Beide blockieren Angriffe, IDS nur intern"],
                    "tip": "IDS = Intrusion Detection System (passiv), IPS = Intrusion Prevention System (aktiv blockierend).",
                    "level": "hard"
                },
                {
                    "q": "Was ist asymmetrische Verschlüsselung?",
                    "opts": ["Öffentlicher Schlüssel zum Verschlüsseln, privater Schlüssel zum Entschlüsseln", "Gleicher Schlüssel zum Ver- und Entschlüsseln", "Zwei identische Schlüssel für beide Seiten", "Kein Schlüssel nötig, Algorithmus reicht"],
                    "tip": "Asymmetrisch: Schlüsselpaar (public/private). Beispiele: RSA, ECC. Basis von HTTPS und PKI.",
                    "level": "hard"
                },
                {
                    "q": "Was ist symmetrische Verschlüsselung?",
                    "opts": ["Gleicher Schlüssel zum Ver- und Entschlüsseln", "Öffentlicher Schlüssel zum Verschlüsseln, privater zum Entschlüsseln", "Kein Schlüssel nötig", "Zwei verschiedene Schlüssel pro Seite"],
                    "tip": "Symmetrisch: ein gemeinsamer Schlüssel. Schnell, aber Schlüsselaustausch ist das Problem. AES, DES.",
                    "level": "hard"
                },
                {
                    "q": "Welchen Port verwendet RDP?",
                    "opts": ["3389", "22", "443", "5900"],
                    "tip": "RDP (Remote Desktop Protocol) nutzt Port 3389. VNC nutzt 5900.",
                    "level": "hard"
                },
                {
                    "q": "Welchen Port verwendet DNS?",
                    "opts": ["53", "443", "80", "123"],
                    "tip": "DNS nutzt Port 53 (UDP und TCP). NTP (Zeitserver) nutzt Port 123.",
                    "level": "hard"
                },
                {
                    "q": "Was ist ein Zero-Day-Exploit?",
                    "opts": ["Ausnutzung einer Schwachstelle, für die noch kein Patch existiert", "Ein Angriff der genau um Mitternacht stattfindet", "Ein frisch installiertes System ohne Konfiguration", "Eine Schwachstelle die seit Jahren bekannt ist"],
                    "tip": "Zero-Day = kein Tag bleibt dem Hersteller zum Reagieren. Kein Patch, kaum Verteidigung.",
                    "level": "hard"
                },
                {
                    "q": "Was macht ein SIEM?",
                    "opts": ["Sammelt und korreliert Log-Daten zentral, um Angriffe zu erkennen", "Blockiert Angriffe in Echtzeit wie eine Firewall", "Verwaltet Benutzerkonten und Passwörter", "Scannt Systeme auf Schwachstellen"],
                    "tip": "SIEM = Security Information and Event Management. Beispiele: Wazuh, Splunk, Microsoft Sentinel.",
                    "level": "hard"
                },
                {
                    "q": "Was ist Multi-Faktor-Authentifizierung (MFA)?",
                    "opts": ["Authentifizierung mit mindestens zwei verschiedenen Faktoren (Wissen, Besitz, Biometrie)", "Authentifizierung mit einem sehr langen Passwort", "Authentifizierung über mehrere Server gleichzeitig", "Authentifizierung mit nur einem starken Faktor"],
                    "tip": "MFA-Faktoren: Wissen (PIN/Passwort), Besitz (Token/Handy), Biometrie (Fingerabdruck).",
                    "level": "hard"
                },
                {
                    "q": "Welche Ports verwendet SMTP?",
                    "opts": ["25 (Server–Server) / 587 (Client–Server, verschlüsselt)", "110 / 995", "143 / 993", "80 / 443"],
                    "tip": "SMTP: 25 (Server–Server), 587 (Submission, STARTTLS). POP3: 110/995. IMAP: 143/993.",
                    "level": "hard"
                },
            ]
        }
    },
    "en": {
        "subtitle":     "IT Quiz Trainer for FiSis  github.com/blamevlan",
        "lang_prompt":  "Sprache / Language (de/en)",
        "menu_title":   "What do you want to practice?",
        "mode1":        "OSI Layers     — assign protocols, devices and functions",
        "mode2":        "Abbreviations  — know and explain IT terms",
        "mode3":        "IT Security    — CIA triad, BSI, concepts, ports",
        "mode_prompt":  "Select (1/2/3)",
        "diff_title":   "Difficulty:",
        "diff1":        "Basics    — fundamentals and common exam topics",
        "diff2":        "Advanced  — all questions including specialist knowledge",
        "diff_prompt":  "Select (1/2)",
        "correct":      "✓ Correct!",
        "wrong":        "✗ Wrong.",
        "correct_ans":  "Correct answer",
        "tip_label":    "Explanation",
        "continue":     "Continue? (Enter = yes, m = menu, q = quit)",
        "result":       "Result:",
        "right_count":  "Correct",
        "wrong_count":  "Wrong",
        "total":        "Total",
        "score_good":   "Well done! You are ready for the exam!",
        "score_mid":    "Not bad — keep practicing!",
        "score_bad":    "Try again — you can do it!",
        "back_hint":    "m = back to menu",
        "input_hint":   "m=menu, q=quit",
        "mc_prompt":    "Select (1/2/3/4)",
        "your_ans":     "Your answer",
        "try_again":    "Try again — no hint yet.",
        "hint_now":     "Hint",
        "last_try":     "Last attempt",
        "attempt":      "Attempt",
        "quit_label":   "Quit",
        "or_label":     "or",
        "round_label":  "Question",
        "all_done":     "All questions answered!",
        "questions": {
            "osi": [
                # ── BASICS ──
                {
                    "q": "On which OSI layer does the IP protocol operate?",
                    "opts": ["Layer 3 — Network", "Layer 2 — Data Link", "Layer 4 — Transport", "Layer 1 — Physical"],
                    "tip": "IP is a Layer 3 protocol. Routers operate at Layer 3.",
                    "level": "easy"
                },
                {
                    "q": "What is OSI layer 7 called?",
                    "opts": ["Application", "Session", "Transport", "Presentation"],
                    "tip": "Layer 7 is the Application layer. HTTP, FTP, DNS and SMTP operate here.",
                    "level": "easy"
                },
                {
                    "q": "What is OSI layer 1 called?",
                    "opts": ["Physical", "Data Link", "Network", "Transport"],
                    "tip": "Layer 1 transmits raw bits over a physical medium. Cables, hubs, repeaters.",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does a switch operate?",
                    "opts": ["Layer 2 — Data Link", "Layer 1 — Physical", "Layer 3 — Network", "Layer 4 — Transport"],
                    "tip": "A switch uses MAC addresses — Layer 2. Layer 3 switches can also route.",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does a router operate?",
                    "opts": ["Layer 3 — Network", "Layer 2 — Data Link", "Layer 4 — Transport", "Layer 7 — Application"],
                    "tip": "Routers forward packets based on IP addresses — that is Layer 3.",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does TCP operate?",
                    "opts": ["Layer 4 — Transport", "Layer 3 — Network", "Layer 2 — Data Link", "Layer 7 — Application"],
                    "tip": "TCP and UDP are transport protocols — Layer 4.",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does HTTP operate?",
                    "opts": ["Layer 7 — Application", "Layer 4 — Transport", "Layer 3 — Network", "Layer 6 — Presentation"],
                    "tip": "HTTP is an application protocol — Layer 7.",
                    "level": "easy"
                },
                {
                    "q": "What is OSI layer 2 called?",
                    "opts": ["Data Link", "Physical", "Network", "Transport"],
                    "tip": "Layer 2 handles transmission between directly connected devices. MAC addresses, Ethernet.",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does a hub operate?",
                    "opts": ["Layer 1 — Physical", "Layer 2 — Data Link", "Layer 3 — Network", "Layer 4 — Transport"],
                    "tip": "A hub forwards all signals to all ports — purely physical, Layer 1.",
                    "level": "easy"
                },
                {
                    "q": "What is OSI layer 4 called?",
                    "opts": ["Transport", "Session", "Network", "Application"],
                    "tip": "Layer 4 handles reliable data transport between systems. TCP and UDP.",
                    "level": "easy"
                },
                {
                    "q": "Which layer is responsible for MAC addresses?",
                    "opts": ["Layer 2 — Data Link", "Layer 3 — Network", "Layer 1 — Physical", "Layer 4 — Transport"],
                    "tip": "MAC addresses are hardware addresses and belong to the Data Link layer (Layer 2).",
                    "level": "easy"
                },
                {
                    "q": "On which OSI layer does UDP operate?",
                    "opts": ["Layer 4 — Transport", "Layer 3 — Network", "Layer 7 — Application", "Layer 2 — Data Link"],
                    "tip": "UDP is a transport protocol like TCP — Layer 4. Fast, connectionless.",
                    "level": "easy"
                },
                # ── ADVANCED ──
                {
                    "q": "On which OSI layer does SSL/TLS operate?",
                    "opts": ["Layer 6 — Presentation", "Layer 4 — Transport", "Layer 7 — Application", "Layer 5 — Session"],
                    "tip": "SSL/TLS encrypts and encodes data — that is the job of the Presentation layer (Layer 6).",
                    "level": "hard"
                },
                {
                    "q": "What is OSI layer 5 called?",
                    "opts": ["Session", "Presentation", "Transport", "Application"],
                    "tip": "Layer 5 establishes, manages and terminates sessions. NetBIOS, RPC.",
                    "level": "hard"
                },
                {
                    "q": "What is OSI layer 6 called?",
                    "opts": ["Presentation", "Session", "Application", "Transport"],
                    "tip": "Layer 6 converts data into a unified format. Encryption, compression, character sets.",
                    "level": "hard"
                },
                {
                    "q": "What is the main function of the Session layer (Layer 5)?",
                    "opts": ["Establishing, managing and terminating communication sessions", "Data encryption and compression", "Forwarding packets based on IP addresses", "Error detection during transmission"],
                    "tip": "Layer 5 coordinates the dialog between two systems — setup, synchronization, teardown.",
                    "level": "hard"
                },
                {
                    "q": "On which OSI layer does DNS operate?",
                    "opts": ["Layer 7 — Application", "Layer 3 — Network", "Layer 4 — Transport", "Layer 5 — Session"],
                    "tip": "DNS is an application protocol — Layer 7.",
                    "level": "hard"
                },
                {
                    "q": "On which OSI layer does SMTP operate?",
                    "opts": ["Layer 7 — Application", "Layer 4 — Transport", "Layer 6 — Presentation", "Layer 3 — Network"],
                    "tip": "SMTP transmits emails — it is an application protocol at Layer 7.",
                    "level": "hard"
                },
                {
                    "q": "What does the Presentation layer (Layer 6) do?",
                    "opts": ["Data encoding, encryption and compression", "Establishing and terminating connections", "Forwarding data packets", "Reliable end-to-end transmission"],
                    "tip": "Layer 6 ensures data is in a readable format for the receiver.",
                    "level": "hard"
                },
                {
                    "q": "On which layer does FTP operate?",
                    "opts": ["Layer 7 — Application", "Layer 4 — Transport", "Layer 3 — Network", "Layer 6 — Presentation"],
                    "tip": "FTP is an application protocol — Layer 7.",
                    "level": "hard"
                },
            ],
            "abk": [
                # ── BASICS ──
                {"q": "What does DNS stand for?", "opts": ["Domain Name System", "Dynamic Network Service", "Data Name Server", "Domain Node System"], "tip": "DNS resolves hostnames to IP addresses.", "level": "easy"},
                {"q": "What does DHCP stand for?", "opts": ["Dynamic Host Configuration Protocol", "Domain Host Control Protocol", "Dynamic Hardware Configuration Protocol", "Data Host Communication Protocol"], "tip": "DHCP automatically assigns IP addresses, subnet mask, gateway and DNS to clients.", "level": "easy"},
                {"q": "What does HTTP stand for?", "opts": ["Hypertext Transfer Protocol", "High Transfer Text Protocol", "Hypertext Transmission Program", "Host Transfer Text Protocol"], "tip": "HTTP is the protocol for web pages. Port 80.", "level": "easy"},
                {"q": "What does HTTPS stand for?", "opts": ["Hypertext Transfer Protocol Secure", "High Transfer Text Protocol Secure", "Hypertext Transmission Protocol System", "Host Transfer Text Protocol Secure"], "tip": "HTTPS is HTTP with TLS encryption. Port 443.", "level": "easy"},
                {"q": "What does TCP stand for?", "opts": ["Transmission Control Protocol", "Transfer Communication Protocol", "Transport Control Program", "Terminal Connection Protocol"], "tip": "TCP provides reliable, ordered transmission with error correction.", "level": "easy"},
                {"q": "What does UDP stand for?", "opts": ["User Datagram Protocol", "Universal Data Protocol", "Unified Datagram Program", "User Data Program"], "tip": "UDP transmits fast without connection setup — no guarantee. Streaming, DNS, VoIP.", "level": "easy"},
                {"q": "What does VPN stand for?", "opts": ["Virtual Private Network", "Virtual Protocol Network", "Verified Private Network", "Virtual Public Network"], "tip": "A VPN encrypts traffic and securely connects networks over the internet.", "level": "easy"},
                {"q": "What does LAN stand for?", "opts": ["Local Area Network", "Long Area Network", "Local Access Node", "Linked Area Network"], "tip": "LAN refers to a local network, e.g. in an office or building.", "level": "easy"},
                {"q": "What does WAN stand for?", "opts": ["Wide Area Network", "Wireless Area Network", "Wide Access Node", "World Area Network"], "tip": "WAN connects networks over large geographic distances. The internet is the largest WAN.", "level": "easy"},
                {"q": "What does SSH stand for?", "opts": ["Secure Shell", "System Shell Handler", "Secure Socket Host", "System Secure Host"], "tip": "SSH enables secure, encrypted remote access to systems. Port 22.", "level": "easy"},
                {"q": "What does FTP stand for?", "opts": ["File Transfer Protocol", "Fast Transfer Protocol", "File Transmission Program", "Full Transfer Protocol"], "tip": "FTP transfers files. Port 21 (control), 20 (data). Unencrypted — use SFTP instead.", "level": "easy"},
                {"q": "What does NAT stand for?", "opts": ["Network Address Translation", "Network Access Technology", "Node Address Transfer", "Network Allocation Table"], "tip": "NAT translates private IP addresses to public ones. Lets many devices share one public IP.", "level": "easy"},
                {"q": "What does MAC stand for (networking)?", "opts": ["Media Access Control", "Machine Access Code", "Media Address Code", "Main Access Control"], "tip": "The MAC address is a hardware address, globally unique (48 bits).", "level": "easy"},
                {"q": "What does WLAN stand for?", "opts": ["Wireless Local Area Network", "Wide Local Area Network", "Wireless Linked Access Node", "Wide Linked Area Network"], "tip": "WLAN is the wireless network standard IEEE 802.11. Colloquially called Wi-Fi.", "level": "easy"},
                {"q": "What does IP stand for?", "opts": ["Internet Protocol", "Internal Protocol", "Interface Program", "Internet Program"], "tip": "IP addresses devices and routes packets. IPv4 (32 bit) and IPv6 (128 bit).", "level": "easy"},
                # ── ADVANCED ──
                {"q": "What does OSPF stand for?", "opts": ["Open Shortest Path First", "Open System Path Finder", "Optimized Shortest Path Forward", "Open Subnet Path First"], "tip": "OSPF is a link-state routing protocol for internal networks (IGP).", "level": "hard"},
                {"q": "What does BGP stand for?", "opts": ["Border Gateway Protocol", "Basic Gateway Protocol", "Border Group Protocol", "Broadband Gateway Protocol"], "tip": "BGP is the routing protocol of the internet — connects autonomous systems (AS).", "level": "hard"},
                {"q": "What does ICMP stand for?", "opts": ["Internet Control Message Protocol", "Internal Control Message Protocol", "Internet Communication Management Protocol", "Integrated Control Message Protocol"], "tip": "ICMP reports network errors and is used by ping and traceroute.", "level": "hard"},
                {"q": "What does ARP stand for?", "opts": ["Address Resolution Protocol", "Automatic Routing Protocol", "Address Routing Program", "Access Resolution Protocol"], "tip": "ARP resolves IP addresses to MAC addresses within the local network.", "level": "hard"},
                {"q": "What does LDAP stand for?", "opts": ["Lightweight Directory Access Protocol", "Local Directory Access Protocol", "Linked Data Access Protocol", "Lightweight Data Application Protocol"], "tip": "LDAP queries directory services. Active Directory is based on LDAP.", "level": "hard"},
                {"q": "What does PKI stand for?", "opts": ["Public Key Infrastructure", "Private Key Interface", "Public Key Interface", "Protocol Key Infrastructure"], "tip": "PKI manages digital certificates and public keys.", "level": "hard"},
                {"q": "What does MFA stand for?", "opts": ["Multi-Factor Authentication", "Multi-Frequency Access", "Managed Factor Authentication", "Multi-Function Application"], "tip": "MFA requires at least two factors: knowledge (PIN), possession (token), biometrics.", "level": "hard"},
                {"q": "What does CVSS stand for?", "opts": ["Common Vulnerability Scoring System", "Central Vulnerability Security System", "Common Vulnerability Security Score", "Centralized Vulnerability Scoring System"], "tip": "CVSS rates vulnerabilities on a scale from 0 to 10.", "level": "hard"},
                {"q": "What does IDS stand for?", "opts": ["Intrusion Detection System", "Internal Defense System", "Integrated Detection System", "Intrusion Defense System"], "tip": "An IDS detects attacks and reports them — does not actively block.", "level": "hard"},
                {"q": "What does IPS stand for?", "opts": ["Intrusion Prevention System", "Internal Protection System", "Integrated Prevention System", "Intrusion Protection Service"], "tip": "An IPS detects attacks and actively blocks them — an evolution of the IDS.", "level": "hard"},
                {"q": "What does VLAN stand for?", "opts": ["Virtual Local Area Network", "Very Local Area Network", "Virtual Linked Access Network", "Variable Local Area Network"], "tip": "VLANs segment a physical network into logical sub-networks at Layer 2.", "level": "hard"},
                {"q": "What does CIDR stand for?", "opts": ["Classless Inter-Domain Routing", "Central Internet Domain Routing", "Common Inter-Domain Routing", "Classless Internet Domain Registry"], "tip": "CIDR replaces Class A/B/C and allows flexible subnet masks.", "level": "hard"},
                {"q": "What does SMTP stand for?", "opts": ["Simple Mail Transfer Protocol", "Secure Mail Transfer Protocol", "Standard Mail Transfer Protocol", "Simple Message Transfer Program"], "tip": "SMTP sends emails. Port 25 (server-to-server), 587 (client-to-server, encrypted).", "level": "hard"},
                {"q": "What does IMAP stand for?", "opts": ["Internet Message Access Protocol", "Internal Mail Access Protocol", "Internet Mail Application Protocol", "Integrated Message Access Protocol"], "tip": "IMAP downloads emails from the server and syncs them. Port 143, encrypted 993.", "level": "hard"},
                {"q": "What does RAID stand for?", "opts": ["Redundant Array of Independent Disks", "Rapid Array of Internal Disks", "Redundant Access of Independent Drives", "Remote Array of Integrated Disks"], "tip": "RAID combines multiple drives for redundancy or performance.", "level": "hard"},
                {"q": "What does SLA stand for?", "opts": ["Service Level Agreement", "System Level Agreement", "Service Linked Application", "Standard Level Agreement"], "tip": "An SLA defines guaranteed service characteristics like availability or response times.", "level": "hard"},
            ],
            "itg": [
                # ── BASICS ──
                {
                    "q": "What do the three letters of the CIA triad stand for?",
                    "opts": ["Confidentiality, Integrity, Availability", "Control, Integrity, Access", "Confidentiality, Integration, Authorization", "Control, Integration, Availability"],
                    "tip": "CIA = Confidentiality, Integrity, Availability — the three core goals of IT security.",
                    "level": "easy"
                },
                {
                    "q": "What does Confidentiality mean in IT security?",
                    "opts": ["Only authorized users can access data", "Data is complete and unaltered", "Systems are available to authorized users", "Every action is traceable"],
                    "tip": "Confidentiality protects data from unauthorized access, e.g. through encryption.",
                    "level": "easy"
                },
                {
                    "q": "What does Integrity mean in IT security?",
                    "opts": ["Data is complete and unaltered", "Only authorized users can access data", "Systems are available to authorized users", "Changes are logged"],
                    "tip": "Integrity ensures data has not been tampered with unnoticed, e.g. through checksums or hashes.",
                    "level": "easy"
                },
                {
                    "q": "What does Availability mean in IT security?",
                    "opts": ["Systems and data are accessible to authorized users when needed", "Data is encrypted and protected", "Changes are logged", "Only authorized users can modify data"],
                    "tip": "Availability means: no outage, no denial of service. Systems must be reachable.",
                    "level": "easy"
                },
                {
                    "q": "What does BSI stand for (Germany)?",
                    "opts": ["Federal Office for Information Security", "Federal Agency for System Integration", "Bureau for Security and Infrastructure", "Federal Office for System Security and IT"],
                    "tip": "The BSI (Bundesamt für Sicherheit in der Informationstechnik) is Germany's national cybersecurity authority.",
                    "level": "easy"
                },
                {
                    "q": "What is the difference between authentication and authorization?",
                    "opts": ["Authentication verifies identity, authorization grants permissions", "Authorization verifies identity, authentication grants permissions", "Both verify the user's identity", "Authorization encrypts the access"],
                    "tip": "First authenticate (who are you?), then authorize (what are you allowed to do?).",
                    "level": "easy"
                },
                {
                    "q": "Which port does HTTPS use?",
                    "opts": ["443", "80", "8080", "8443"],
                    "tip": "HTTP uses port 80, HTTPS uses port 443.",
                    "level": "easy"
                },
                {
                    "q": "Which port does SSH use?",
                    "opts": ["22", "23", "21", "3389"],
                    "tip": "SSH uses port 22 by default. Telnet (insecure) uses port 23.",
                    "level": "easy"
                },
                {
                    "q": "What is a vulnerability?",
                    "opts": ["A weakness in a system that can be exploited", "An active attack on a system", "A security patch", "An intruder in the network"],
                    "tip": "Vulnerability = weakness. Threat = potential danger. Risk = probability × impact.",
                    "level": "easy"
                },
                {
                    "q": "What is a backup?",
                    "opts": ["A saved copy of data for restoration", "An encryption of data", "A data transfer protocol", "A method for access control"],
                    "tip": "Backups protect against data loss from ransomware, hardware failure or human mistakes.",
                    "level": "easy"
                },
                # ── ADVANCED ──
                {
                    "q": "What is the difference between IDS and IPS?",
                    "opts": ["IDS detects and reports attacks, IPS detects and actively blocks them", "IPS detects and reports attacks, IDS actively blocks them", "IDS is for networks, IPS is for hosts", "Both block attacks, IDS only internally"],
                    "tip": "IDS = Intrusion Detection System (passive), IPS = Intrusion Prevention System (active blocking).",
                    "level": "hard"
                },
                {
                    "q": "What is asymmetric encryption?",
                    "opts": ["Public key encrypts, private key decrypts", "Same key for both encryption and decryption", "Two identical keys for both sides", "No key needed, algorithm is sufficient"],
                    "tip": "Asymmetric: key pair (public/private). Examples: RSA, ECC. Basis of HTTPS and PKI.",
                    "level": "hard"
                },
                {
                    "q": "What is symmetric encryption?",
                    "opts": ["Same key for both encryption and decryption", "Public key encrypts, private key decrypts", "No key needed", "Two different keys per side"],
                    "tip": "Symmetric: one shared key. Fast, but key exchange is the challenge. AES, DES.",
                    "level": "hard"
                },
                {
                    "q": "Which port does RDP use?",
                    "opts": ["3389", "22", "443", "5900"],
                    "tip": "RDP (Remote Desktop Protocol) uses port 3389. VNC uses 5900.",
                    "level": "hard"
                },
                {
                    "q": "Which port does DNS use?",
                    "opts": ["53", "443", "80", "123"],
                    "tip": "DNS uses port 53 (UDP and TCP). NTP (time server) uses port 123.",
                    "level": "hard"
                },
                {
                    "q": "What is a zero-day exploit?",
                    "opts": ["Exploiting a vulnerability for which no patch exists yet", "An attack that takes place exactly at midnight", "A freshly installed system without configuration", "A vulnerability that has been known for years"],
                    "tip": "Zero-day = the vendor has zero days to react. No patch, no defense except detection.",
                    "level": "hard"
                },
                {
                    "q": "What does a SIEM do?",
                    "opts": ["Centrally collects and correlates log data to detect attacks", "Blocks attacks in real time like a firewall", "Manages user accounts and passwords", "Scans systems for vulnerabilities"],
                    "tip": "SIEM = Security Information and Event Management. Examples: Wazuh, Splunk, Microsoft Sentinel.",
                    "level": "hard"
                },
                {
                    "q": "What is multi-factor authentication (MFA)?",
                    "opts": ["Authentication using at least two different factors (knowledge, possession, biometrics)", "Authentication with a very long password", "Authentication across multiple servers simultaneously", "Authentication with only one strong factor"],
                    "tip": "MFA factors: knowledge (PIN/password), possession (token/phone), biometrics (fingerprint).",
                    "level": "hard"
                },
                {
                    "q": "Which ports does SMTP use?",
                    "opts": ["25 (server-to-server) / 587 (client-to-server, encrypted)", "110 / 995", "143 / 993", "80 / 443"],
                    "tip": "SMTP: 25 (server-to-server), 587 (submission, STARTTLS). POP3: 110/995. IMAP: 143/993.",
                    "level": "hard"
                },
            ]
        }
    }
}

T = LANG["de"]

# ── Hilfsfunktionen ────────────────────────────────────────────────────────────
class BackToMenu(Exception): pass

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"{BLU}{BLD}")
    print("  ██████╗ ██╗   ██╗██╗███████╗")
    print("  ██╔═══██╗██║   ██║██║╚════██║")
    print("  ██║   ██║██║   ██║██║    ██╔╝")
    print("  ██║▄▄ ██║██║   ██║██║   ██╔╝ ")
    print("  ╚██████╔╝╚██████╔╝██║   ██║  ")
    print("   ╚══▀▀═╝  ╚═════╝ ╚═╝   ╚═╝  ")
    print(f"  {YLW}{T['subtitle']}{RST}")
    print()

def hinweis_zeile(extra=""):
    h = f"{DIM}  ┌ q = {T['quit_label']}"
    if extra:
        h += f"  │  {extra}"
    h += f"{RST}"
    print(h)

def sprachauswahl():
    global T
    print(f"  {BLD}Sprache / Language:{RST}")
    print(f"  {GRN}[de]{RST} Deutsch")
    print(f"  {BLU}[en]{RST} English")
    print()
    hinweis_zeile()
    while True:
        try:
            wahl = input(f"  {CYN}▶ {LANG['de']['lang_prompt']}: {RST}").strip().lower()
        except EOFError:
            raise SystemExit
        if wahl in ("de", "en"):
            T = LANG[wahl]
            return
        if wahl == "q":
            raise SystemExit
        print(f"  {RED}Bitte 'de' {LANG['de']['or_label']} 'en' eingeben.{RST}")

def hauptmenue():
    print(f"  {BLD}{T['menu_title']}{RST}")
    print(f"  {GRN}[1]{RST} {T['mode1']}")
    print(f"  {YLW}[2]{RST} {T['mode2']}")
    print(f"  {RED}[3]{RST} {T['mode3']}")
    print(f"  {DIM}[l]{RST} Sprache / Language")
    print()
    hinweis_zeile()
    while True:
        try:
            wahl = input(f"  {CYN}▶ {T['mode_prompt']}: {RST}").strip().lower()
        except EOFError:
            return "q"
        if wahl in ("1", "2", "3", "l", "q"):
            return wahl
        print(f"  {RED}1, 2, 3, l {T['or_label']} q.{RST}")

def schwierigkeitsmenue():
    print(f"  {BLD}{T['diff_title']}{RST}")
    print(f"  {GRN}[1]{RST} {T['diff1']}")
    print(f"  {YLW}[2]{RST} {T['diff2']}")
    print()
    hinweis_zeile(T['back_hint'])
    while True:
        try:
            wahl = input(f"  {CYN}▶ {T['diff_prompt']}: {RST}").strip().lower()
        except EOFError:
            return 1
        if wahl == "m":
            raise BackToMenu()
        if wahl == "q":
            raise SystemExit
        if wahl in ("1", "2"):
            return int(wahl)
        print(f"  {RED}1 {T['or_label']} 2.{RST}")

def frage_stellen(frage_dict, nummer, gesamt):
    opts = frage_dict["opts"][:]
    richtig_text = opts[0]
    random.shuffle(opts)
    richtig_buchstabe = LETTERS[opts.index(richtig_text)]
    max_versuche = 3

    def zeige_frage(versuch):
        print(f"  {DIM}{T['round_label']} {nummer}/{gesamt}  |  {T['attempt']} {versuch}/{max_versuche}{RST}\n")
        print(f"  {BLD}{frage_dict['q']}{RST}\n")
        for i, opt in enumerate(opts):
            print(f"  {YLW}[{LETTERS[i]}]{RST} {opt}")
        print()
        hinweis_zeile(T['back_hint'])

    for versuch in range(1, max_versuche + 1):
        zeige_frage(versuch)

        while True:
            try:
                wahl = input(f"  {CYN}▶ {T['mc_prompt']}: {RST}").strip().upper()
            except EOFError:
                raise SystemExit
            if wahl == "M":
                raise BackToMenu()
            if wahl == "Q":
                raise SystemExit
            if wahl in LETTERS:
                break
            print(f"  {RED}1, 2, 3 {T['or_label']} 4.{RST}")

        if wahl == richtig_buchstabe:
            print(f"\n  {GRN}{T['correct']}{RST}")
            return versuch == 1  # nur erster Versuch zählt als richtig

        gewaehlter_text = opts[LETTERS.index(wahl)]
        print(f"\n  {RED}{T['wrong']}{RST}")
        print(f"  {RED}{T['your_ans']}: {BLD}{gewaehlter_text}{RST}")

        if versuch == 1:
            print(f"  {YLW}{T['try_again']}{RST}")
        elif versuch == 2:
            print(f"  {YLW}{T['hint_now']}: {frage_dict['tip']}{RST}")
            print(f"  {DIM}{T['last_try']}...{RST}")
        else:
            print(f"  {GRN}{T['correct_ans']}: {BLD}{richtig_text}{RST}")
            print(f"  {DIM}{T['tip_label']}: {frage_dict['tip']}{RST}")
            return False

        print()
        if versuch < max_versuche:
            try:
                input(f"  {CYN}▶ Enter: {RST}")
            except EOFError:
                raise SystemExit
        clear(); banner()
        g_temp = 0
        print(f"  {DIM}{'─'*60}{RST}\n")

    return False

def zeige_ergebnis(richtig, falsch):
    clear(); banner()
    g = richtig + falsch
    p = round(richtig / g * 100) if g > 0 else 0
    print(f"  {BLD}{T['result']}{RST}")
    print(f"  {T['right_count']}: {GRN}{richtig}{RST}  |  {T['wrong_count']}: {RED}{falsch}{RST}  |  {T['total']}: {g}")
    print(f"  Score: {YLW}{BLD}{p}%{RST}\n")
    if p >= 80:   print(f"  {GRN}{BLD}{T['score_good']}{RST}")
    elif p >= 50: print(f"  {YLW}{T['score_mid']}{RST}")
    else:         print(f"  {RED}{T['score_bad']}{RST}")
    print()

def modus_quiz(mode_key):
    try:
        schwierigkeit = schwierigkeitsmenue()
    except BackToMenu:
        return 0, 0

    alle = T["questions"][mode_key]
    pool = [f for f in alle if f["level"] == "easy"] if schwierigkeit == 1 else alle[:]
    random.shuffle(pool)

    richtig = 0; falsch = 0

    for i, frage in enumerate(pool):
        clear(); banner()
        g = richtig + falsch
        p = round(richtig / g * 100) if g > 0 else 0
        print(f"  {GRN}{richtig}{RST}✓  {RED}{falsch}{RST}✗  |  {YLW}{p}%{RST}\n")

        try:
            ok = frage_stellen(frage, i + 1, len(pool))
        except BackToMenu:
            return richtig, falsch

        if ok:
            richtig += 1
        else:
            falsch += 1

        if i == len(pool) - 1:
            print(f"\n  {MGN}{T['all_done']}{RST}")

        print()
        try:
            weiter = input(f"  {CYN}▶ {T['continue']}: {RST}").strip().lower()
        except EOFError:
            weiter = "q"

        if weiter == "q":
            zeige_ergebnis(richtig, falsch)
            raise SystemExit
        elif weiter == "m":
            return richtig, falsch

    zeige_ergebnis(richtig, falsch)
    return richtig, falsch

# ── Hauptprogramm ──────────────────────────────────────────────────────────────
MODE_KEYS = {"1": "osi", "2": "abk", "3": "itg"}

def main():
    clear(); banner()
    sprachauswahl()

    while True:
        clear(); banner()
        wahl = hauptmenue()

        if wahl == "q":
            break
        if wahl == "l":
            clear(); banner()
            sprachauswahl()
            continue

        modus_quiz(MODE_KEYS[wahl])

if __name__ == "__main__":
    main()
