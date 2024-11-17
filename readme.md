
# Unsafe API

Diese API wurde absichtlich entwickelt, um Schwachstellen aus den [OWASP API Top 10](https://owasp.org/www-project-api-security/) zu demonstrieren. Sie dient ausschließlich zu **Bildungszwecken**, um Entwicklern und Sicherheitsexperten zu zeigen, wie Sicherheitslücken entstehen und wie sie ausgenutzt werden können.

---

## **Inhalt**
1. [Funktionalität](#funktionalität)
2. [Installationsanweisungen](#installationsanweisungen)
3. [API starten](#api-starten)
4. [API-Endpunkte](#api-endpunkte)
5. [Bekannte Sicherheitslücken](#bekannte-sicherheitslücken)
6. [Warnung](#warnung)

---

## **Funktionalität**
Die API bietet mehrere absichtlich unsichere Funktionen:
- **Unrestricted Resource Consumption**: Eine unlimitierte Berechnung von Ressourcen.
- **Server-Side Request Forgery (SSRF)**: Führt unkontrollierte Anfragen an externe oder interne URLs aus.
- **Security Misconfiguration**: Debugging-Daten und sensible Konfigurationen werden öffentlich preisgegeben.
- **Unsafe Consumption of APIs**: Eingaben werden nicht validiert, was zu unerwartetem Verhalten führt.

---

## **Installationsanweisungen**

1. **Voraussetzungen**:
   - Python 3.11.7
   - Paketmanager `pip`

2. **Projekt klonen oder herunterladen**:
   ```bash
   git clone https://github.com/Jxshyz/unsafeAPI.git
   cd unsafeAPI
   ```

3. **Abhängigkeiten installieren**:
   Stelle sicher, dass alle benötigten Pakete installiert sind:
   ```bash
   pip install -r requirements.txt
   ```

---

## **API starten**
1. **Starten der API**:
   ```bash
   python vulnerable_api.py
   ```

2. **Standardadresse**:
   Die API läuft unter:
   ```
   http://127.0.0.1:5000
   ```

3. **Alternativer Port**:
   Du kannst die API auf einem anderen Port starten:
   ```bash
   python vulnerable_api.py --port 8080
   ```

---

## **API-Endpunkte**

### 1. **Unrestricted Resource Consumption**
- **Route**: `GET /factorial/<num>`
- **Beschreibung**: Berechnet die Fakultät der Zahl `<num>` ohne Begrenzung, was zu einer Überlastung des Servers führen kann.
- **Beispiel**:
  ```bash
  curl http://127.0.0.1:5000/factorial/10
  ```
- **Antwort**:
  ```json
  {
    "number": 10,
    "factorial": 3628800
  }
  ```

---

### 2. **Server-Side Request Forgery (SSRF)**
- **Route**: `POST /fetch_url`
- **Beschreibung**: Führt eine HTTP-Anfrage an eine vom Benutzer angegebene URL aus. Dies ermöglicht Angriffe wie interne Netzwerkscans.
- **Beispiel**:
  ```bash
  curl -X POST http://127.0.0.1:5000/fetch_url -H "Content-Type: application/json" -d '{"url": "http://example.com"}'
  ```
- **Antwort**:
  ```json
  {
    "status": 200,
    "content": "..."
  }
  ```

---

### 3. **Security Misconfiguration**
- **Route**: `GET /debug`
- **Beschreibung**: Gibt Debug-Informationen und sensible Konfigurationsdetails wie API-Keys aus.
- **Beispiel**:
  ```bash
  curl http://127.0.0.1:5000/debug
  ```
- **Antwort**:
  ```json
  {
    "debug": true,
    "database_url": "postgresql://user:password@localhost/db",
    "api_key": "supersecretapikey123"
  }
  ```

---

### 4. **Unsafe Consumption of APIs**
- **Route**: `POST /add_numbers`
- **Beschreibung**: Addiert zwei Zahlen, prüft die Eingaben jedoch nicht. Fehlerhafte Eingaben können die API zum Absturz bringen.
- **Beispiel**:
  ```bash
  curl -X POST http://127.0.0.1:5000/add_numbers -H "Content-Type: application/json" -d '{"num1": 5, "num2": 10}'
  ```
- **Antwort**:
  ```json
  {
    "result": 15
  }
  ```

---

## **Bekannte Sicherheitslücken**

### 1. **Unrestricted Resource Consumption**
- Die Route `/factorial/<num>` akzeptiert beliebig große Zahlen. Dies kann zu hoher CPU-Auslastung und Speicherproblemen führen.

### 2. **Server-Side Request Forgery (SSRF)**
- Die Route `/fetch_url` akzeptiert URLs ohne Filterung. Angreifer können interne Netzwerke scannen oder schädliche URLs aufrufen.

### 3. **Security Misconfiguration**
- Debugging ist aktiviert, wodurch sensible Daten wie API-Keys und Datenbank-URLs öffentlich sichtbar sind.

### 4. **Unsafe Consumption of APIs**
- Die Route `/add_numbers` validiert keine JSON-Daten. Fehlerhafte oder manipulierte Eingaben können unerwartetes Verhalten verursachen.

---

## **Warnung**
**Diese API ist absichtlich unsicher!**
- Verwende diese API nur für Sicherheitsübungen.
- Nutze sie niemals in einer produktiven Umgebung.
- Die API enthält absichtliche Schwachstellen und soll zum Testen und Lernen verwendet werden.

---

## **Lizenz**
Dieses Projekt steht unter der MIT-Lizenz. Es wird keine Haftung für Schäden übernommen, die durch den Missbrauch dieser API entstehen.