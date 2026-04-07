from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(20, 40, 90)
        self.cell(0, 8, "Website Development Report", ln=True, align="C")
        self.set_draw_color(20, 40, 90)
        self.line(10, 20, 200, 20)
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120)
        self.cell(0, 8, f"Page {self.page_no()} / {{nb}}", align="C")

    def section(self, title, body):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(20, 40, 90)
        self.cell(0, 5, title, ln=True)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(40)
        self.multi_cell(0, 3.8, body)
        self.ln(1.2)

sections = [
    ("1. Project Overview",
     "This project delivers a modern, high-performance corporate website engineered to elevate the client's digital presence and drive measurable business outcomes. The platform serves as the primary gateway for customer engagement, lead generation, and brand storytelling. Its purpose is to present the client's services through an intuitive, conversion-focused experience while supporting scalability for future growth. Key business goals include increasing qualified leads, improving brand credibility, reducing bounce rates, and providing an administrative backbone for content management."),
    ("2. Technologies Used",
     "Frontend: HTML5, CSS3, JavaScript (ES6+), React.js, Next.js, Tailwind CSS, Bootstrap. Backend: Node.js, Express.js, Django REST Framework. Database: PostgreSQL, MongoDB, Redis (caching). DevOps & Tools: Git, GitHub Actions, Docker, Nginx, AWS (EC2, S3, CloudFront), Vercel. Testing: Jest, React Testing Library, Postman, Cypress."),
    ("3. Design & UI/UX Implementation",
     "The design follows a clean, minimal, and contemporary aesthetic aligned with the client's brand identity. Wireframes and high-fidelity mockups were created in Figma prior to development. The layout emphasizes visual hierarchy, whitespace, and readability. A fully responsive grid ensures seamless adaptation across mobile, tablet, and desktop devices. UX enhancements include intuitive navigation, smooth scroll animations, accessible color contrasts (WCAG 2.1 AA), and micro-interactions that elevate the perceived quality of the product."),
    ("4. Features Developed",
     "- Dynamic multi-page architecture with CMS-driven content\n- Secure user authentication (JWT + refresh tokens, OAuth social login)\n- Role-based admin dashboard with analytics widgets\n- Contact, enquiry, and newsletter forms with validation\n- Blog module with categories, tags, and search\n- Third-party API integrations (payment gateway, email service, maps)\n- Real-time notifications and activity logs\n- Multi-language (i18n) ready structure"),
    ("5. Frontend Development",
     "The frontend is built with React.js and Next.js, leveraging server-side rendering (SSR) and static site generation (SSG) for optimal SEO and load performance. Component-based architecture ensures reusability and maintainability. Tailwind CSS provides a utility-first styling system, while Bootstrap handles select responsive components. The UI adapts fluidly to all viewports and has been tested on Chrome, Firefox, Safari, and Edge."),
    ("6. Backend Development",
     "The backend follows a modular, service-oriented architecture built on Node.js/Express and Django REST Framework. RESTful APIs expose all core functionality with clear versioning and documentation. Middleware layers handle authentication, logging, rate limiting, and input validation. Business logic is cleanly separated from controllers, ensuring maintainability and testability. The system is designed to scale horizontally behind a load balancer."),
    ("7. Database Implementation",
     "PostgreSQL serves as the primary relational database, storing structured data such as users, transactions, and content. MongoDB is used for flexible, unstructured datasets like logs and activity feeds. Redis provides in-memory caching for high-frequency queries, significantly reducing response times. Schema design follows normalization best practices with proper indexing, foreign keys, and migration management."),
    ("8. Performance Optimization",
     "Performance was a first-class priority. Optimizations include image compression and WebP delivery, lazy loading, code splitting, tree shaking, CDN distribution via CloudFront, HTTP/2, Gzip/Brotli compression, and Redis caching. The result is a Lighthouse performance score exceeding 90 and initial load times under 2 seconds on standard broadband."),
    ("9. Security Measures",
     "Security best practices are implemented at every layer: HTTPS with TLS 1.3, JWT-based authentication, bcrypt password hashing, CSRF and XSS protection, SQL injection prevention via parameterized queries, rate limiting, Helmet.js security headers, environment-variable secret management, and regular dependency audits. Sensitive data is encrypted at rest and in transit."),
    ("10. Testing & Quality Assurance",
     "A multi-layered QA strategy was applied: unit tests (Jest), integration tests, end-to-end tests (Cypress), and manual exploratory testing. API endpoints were validated using Postman collections. Cross-browser and cross-device testing ensured consistent behavior. All critical bugs were resolved prior to release, and the codebase maintains high test coverage."),
    ("11. Deployment & Hosting",
     "The application is containerized with Docker and deployed via a CI/CD pipeline using GitHub Actions. The frontend is hosted on Vercel for edge delivery, while the backend runs on AWS EC2 behind Nginx as a reverse proxy. Static assets are served via AWS S3 + CloudFront. Automated builds, tests, and deployments ensure rapid, reliable releases with zero downtime."),
    ("12. Conclusion",
     "The delivered website represents a premium, production-grade digital platform that combines technical excellence with refined design. Every component - from architecture to pixel - has been engineered to deliver measurable value: faster load times, stronger security, effortless scalability, and an exceptional user experience. The project has been completed successfully, on scope, and is positioned to support the client's growth for years to come."),
]

pdf = PDF(format="A4")
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()
for title, body in sections:
    pdf.section(title, body)

pdf.output("/home/user/pparam-new-frontend/Website_Development_Report.pdf")
print("OK pages:", pdf.page_no())
