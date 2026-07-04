import whois
import tldextract


def check_domain(domain_url):
    extracted = tldextract.extract(domain_url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    try:
        info = whois.whois(domain)

        return {
            "exists": bool(info.domain_name),
            "domain": domain,
            "creation_date": info.creation_date,
            "registrar": info.registrar,
            "error": None
        }

    except Exception as e:
        print("WHOIS ERROR:", e)
        return {
            "exists": None,
            "domain": domain,
            "creation_date": None,
            "registrar": None,
            "error": str(e)
        }