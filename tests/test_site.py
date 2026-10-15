from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
    def handle_data(self, text):
        self.text.append(text)

class SiteTests(unittest.TestCase):
    def test_home_is_a_static_draft_information_page(self):
        path = ROOT / 'index.html'
        self.assertTrue(path.is_file(), 'The public information home page is missing')
        doc = Document()
        doc.feed(path.read_text())
        visible = ' '.join(doc.text)
        self.assertIn('nbfinance', visible)
        self.assertIn('Draft', visible)
        self.assertIn('No bank connection', visible)
        self.assertIn('Do not use these drafts for live bank registration', visible)
        self.assertTrue(any(tag == 'main' for tag, _ in doc.elements))
        self.assertFalse(any(tag in ['script', 'form', 'input', 'iframe'] for tag, _ in doc.elements))

    def test_privacy_is_a_draft_with_hosting_disclosure(self):
        path = ROOT / 'privacy.html'
        self.assertTrue(path.is_file(), 'The privacy draft is missing')
        doc = Document()
        doc.feed(path.read_text())
        visible = ' '.join(doc.text)
        self.assertIn('Draft', visible)
        self.assertIn('GitHub Pages', visible)
        self.assertIn('IP addresses', visible)
        self.assertIn('security purposes', visible)
        self.assertIn('Final application processing remains pending', visible)
        self.assertIn('Do not use these drafts for live bank registration', visible)
        self.assertIn('No authorisation callback is hosted here', visible)
        self.assertTrue(any(tag == 'a' and attrs.get('href') == 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement' for tag, attrs in doc.elements))

    def test_usage_notice_is_draft_and_has_no_banking_flow(self):
        path = ROOT / 'terms.html'
        self.assertTrue(path.is_file(), 'The usage draft is missing')
        doc = Document()
        doc.feed(path.read_text())
        visible = ' '.join(doc.text)
        self.assertIn('Draft', visible)
        self.assertIn('Do not use these drafts for live bank registration', visible)
        self.assertIn('No live banking service is offered here', visible)
        self.assertIn('not a spending allowance', visible)
        self.assertIn('Final application processing remains pending', visible)
        self.assertFalse(any(tag in ['script', 'form', 'input', 'iframe'] for tag, _ in doc.elements))

    def test_every_page_has_safe_metadata_and_local_navigation(self):
        for name in ['index.html', 'privacy.html', 'terms.html']:
            with self.subTest(page=name):
                source = (ROOT / name).read_text()
                doc = Document()
                doc.feed(source)
                self.assertTrue(source.lower().startswith('<!doctype html>'))
                self.assertEqual(sum(tag == 'h1' for tag, _ in doc.elements), 1)
                self.assertTrue(any(tag == 'html' and attrs.get('lang') == 'en' for tag, attrs in doc.elements))
                self.assertTrue(any(tag == 'meta' and attrs.get('name') == 'viewport' for tag, attrs in doc.elements))
                self.assertTrue(any(tag == 'meta' and attrs.get('name') == 'referrer' and attrs.get('content') == 'no-referrer' for tag, attrs in doc.elements))
                self.assertTrue(any(tag == 'meta' and attrs.get('http-equiv') == 'Content-Security-Policy' and "default-src 'none'" in attrs.get('content', '') and "form-action 'none'" in attrs.get('content', '') for tag, attrs in doc.elements))
                self.assertFalse(any(tag in ['script', 'form', 'input', 'iframe', 'object', 'embed'] for tag, _ in doc.elements))
                for tag, attrs in doc.elements:
                    self.assertFalse(any(key.lower().startswith('on') for key in attrs))
                    self.assertNotIn('style', attrs)
                    if tag == 'link':
                        self.assertEqual(attrs.get('href'), 'styles.css')
                    if tag == 'a':
                        target = attrs.get('href', '')
                        self.assertFalse(target.lower().startswith(('javascript:', 'data:')))
                        if target.lower().startswith('mailto:'):
                            self.assertEqual(target, 'mailto:security@nbsystems.dev')
                        elif target and not target.startswith(('https://', '#')):
                            self.assertTrue((ROOT / target).is_file(), target)

    def test_public_pages_have_only_approved_contact_and_no_bank_ids_or_private_keys(self):
        import re
        for name in ['index.html', 'privacy.html', 'terms.html']:
            with self.subTest(page=name):
                source = (ROOT / name).read_text()
                self.assertEqual(set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', source)), {'security@nbsystems.dev'})
                self.assertIsNone(re.search(r'\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b', source))
                self.assertIsNone(re.search(r'-{5}BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-{5}', source))
                self.assertNotIn('/home/', source)
                self.assertNotIn('accounts[].', source)

    def test_approved_operator_is_visible_on_every_page_without_finalising_drafts(self):
        for name in ['index.html', 'privacy.html', 'terms.html']:
            with self.subTest(page=name):
                source = (ROOT / name).read_text()
                doc = Document()
                doc.feed(source)
                visible = ' '.join(' '.join(doc.text).split())
                self.assertEqual(visible.count('Bernhard Slatinsek'), 1)
                self.assertIn('Operator', visible)
                self.assertIn('Private household project', visible)
                self.assertIn('Final application processing remains pending', visible)
                self.assertIn('Do not use these drafts for live bank registration', visible)
                self.assertNotIn('Operator identity and final application processing remain pending', source)
                self.assertNotIn('Operator details are pending', source)
                self.assertNotIn('operator identity still', source)
                self.assertIn('security@nbsystems.dev', visible)

    def test_approved_contact_is_visible_with_exact_mailto_on_every_page(self):
        for name in ['index.html', 'privacy.html', 'terms.html']:
            with self.subTest(page=name):
                doc = Document()
                doc.feed((ROOT / name).read_text())
                self.assertIn('security@nbsystems.dev', ' '.join(doc.text))
                self.assertTrue(any(tag == 'a' and attrs.get('href') == 'mailto:security@nbsystems.dev' for tag, attrs in doc.elements))

if __name__ == '__main__':
    unittest.main()
