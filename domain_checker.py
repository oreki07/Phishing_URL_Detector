import whois
import tldextract


def check_domain(domain_url):
    try:
        extracted = tldextract.extract(domain_url)

        domain = f"{extracted.domain}.{extracted.suffix}"

        info = whois.whois(domain)

        if info.domain_name:
            return {
                "exists": True,
                "domain": domain,
                "creation_date": info.creation_date,
                "registrar": info.registrar
            }

    except Exception:
        return {
            "exists": False,
            "domain": domain_url
        }