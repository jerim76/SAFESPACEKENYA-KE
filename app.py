<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safe Space Kenya | Professional Therapy & Counseling Services</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2a7a7c; /* Calming teal */
            --secondary: #4a9ca5; /* Soft blue */
            --accent: #d4a373; /* Warm terracotta */
            --light: #f8f9fa;
            --dark: #2c3e50; /* Deep blue for text */
            --gray: #6c757d;
            --light-gray: #e9ecef;
            --highlight: #e8f4f8; /* Soft blue highlight */
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Nunito', sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background-color: #fafafa;
            overflow-x: hidden;
        }

        h1, h2, h3, h4 {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--primary);
        }

        p {
            margin-bottom: 1rem;
        }

        a {
            text-decoration: none;
            color: var(--primary);
            transition: var(--transition);
        }

        a:hover {
            color: var(--accent);
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }

        .btn {
            display: inline-block;
            padding: 12px 28px;
            background-color: var(--primary);
            color: white;
            border-radius: 30px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            font-size: 0.9rem;
        }

        .btn:hover {
            background-color: var(--accent);
            color: white;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .btn-outline {
            background-color: transparent;
            border: 2px solid var(--primary);
            color: var(--primary);
        }

        .btn-outline:hover {
            background-color: var(--primary);
            color: white;
        }

        /* Header Styles */
        header {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            background-color: rgba(255, 255, 255, 0.98);
            box-shadow: var(--shadow);
            padding: 15px 0;
            transition: var(--transition);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
        }

        .logo h1 {
            font-size: 1.8rem;
            margin-bottom: 0;
            color: var(--primary);
        }

        .logo-icon {
            color: var(--primary);
            font-size: 2.2rem;
            margin-right: 10px;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 30px;
        }

        .nav-links a {
            color: var(--dark);
            font-weight: 600;
            position: relative;
        }

        .nav-links a:after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background-color: var(--accent);
            transition: var(--transition);
        }

        .nav-links a:hover:after {
            width: 100%;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--primary);
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(42, 122, 124, 0.85), rgba(42, 122, 124, 0.9)), url('https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?ixlib=rb-4.0.3') center/cover no-repeat;
            height: 100vh;
            display: flex;
            align-items: center;
            color: white;
            text-align: center;
            padding-top: 70px;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            color: white;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-btns {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        /* Services Section */
        .section {
            padding: 100px 0;
        }

        .section-header {
            text-align: center;
            max-width: 700px;
            margin: 0 auto 60px;
        }

        .section-header h2 {
            font-size: 2.5rem;
            position: relative;
            padding-bottom: 15px;
        }

        .section-header h2:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 3px;
            background-color: var(--accent);
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .service-card {
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
            border-top: 4px solid var(--secondary);
        }

        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .service-img {
            height: 200px;
            background-color: var(--highlight);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-size: 3rem;
        }

        .service-content {
            padding: 25px;
        }

        .service-content h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
        }

        .service-content .learn-more {
            display: block;
            margin-top: 20px;
            color: var(--primary);
            font-weight: 600;
            cursor: pointer;
        }

        /* Service Detail Modals */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            z-index: 2000;
            overflow-y: auto;
            padding: 20px;
        }

        .modal-content {
            background-color: white;
            border-radius: 10px;
            max-width: 800px;
            margin: 50px auto;
            position: relative;
            animation: modalopen 0.5s;
        }

        @keyframes modalopen {
            from {opacity: 0; transform: translateY(-50px);}
            to {opacity: 1; transform: translateY(0);}
        }

        .modal-header {
            padding: 20px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border-radius: 10px 10px 0 0;
        }

        .modal-header h3 {
            color: white;
            font-size: 1.8rem;
        }

        .close-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 1.5rem;
            color: white;
            cursor: pointer;
            transition: var(--transition);
        }

        .close-btn:hover {
            color: var(--accent);
        }

        .modal-body {
            padding: 30px;
        }

        .modal-body h4 {
            color: var(--primary);
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .modal-body ul {
            margin-left: 20px;
            margin-bottom: 20px;
        }

        .modal-body li {
            margin-bottom: 10px;
        }

        /* About Section */
        .about {
            background-color: var(--light);
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-text h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .about-image {
            border-radius: 10px;
            overflow: hidden;
            box-shadow: var(--shadow);
            background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
            position: relative;
        }

        .about-image:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://images.unsplash.com/photo-1582560477817-7d9d0a1cdf1f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80') center/cover no-repeat;
            opacity: 0.8;
        }

        /* Team Section */
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }

        .team-member {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: var(--shadow);
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .team-member:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
        }

        .team-member:after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background-color: var(--accent);
        }

        .member-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 20px;
            background-color: var(--highlight);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-size: 3rem;
            border: 3px solid var(--secondary);
        }

        .member-name {
            font-size: 1.3rem;
            margin-bottom: 5px;
        }

        .member-role {
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 15px;
            font-style: italic;
        }

        /* Testimonials */
        .testimonials {
            background: linear-gradient(rgba(42, 122, 124, 0.9), rgba(42, 122, 124, 0.95)), url('https://images.unsplash.com/photo-1503376780353-7e6692767b70?ixlib=rb-4.0.3') center/cover no-repeat;
            color: white;
        }

        .testimonials .section-header h2 {
            color: white;
        }

        .testimonial-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 40px;
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .testimonial-text {
            font-size: 1.2rem;
            font-style: italic;
            margin-bottom: 30px;
            line-height: 1.8;
            position: relative;
        }

        .testimonial-text:before, .testimonial-text:after {
            content: '"';
            font-size: 3rem;
            color: rgba(255, 255, 255, 0.3);
            position: absolute;
        }

        .testimonial-text:before {
            top: -20px;
            left: -15px;
        }

        .testimonial-text:after {
            bottom: -40px;
            right: -15px;
        }

        .testimonial-author {
            font-weight: 600;
            font-size: 1.1rem;
            color: var(--accent);
        }

        /* Contact Section */
        .contact-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .contact-item {
            display: flex;
            gap: 15px;
            align-items: flex-start;
        }

        .contact-icon {
            background: var(--highlight);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-size: 1.2rem;
            flex-shrink: 0;
        }

        .contact-text h4 {
            margin-bottom: 5px;
        }

        .contact-form {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid var(--light-gray);
            border-radius: 5px;
            transition: var(--transition);
            font-family: 'Nunito', sans-serif;
        }

        .form-control:focus {
            border-color: var(--primary);
            outline: none;
            box-shadow: 0 0 0 3px rgba(42, 122, 124, 0.1);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        /* Footer */
        footer {
            background-color: var(--dark);
            color: white;
            padding: 70px 0 20px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }

        .footer-col h3 {
            color: white;
            font-size: 1.4rem;
            margin-bottom: 20px;
            position: relative;
            padding-bottom: 10px;
        }

        .footer-col h3:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 50px;
            height: 2px;
            background-color: var(--accent);
        }

        .footer-links {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 10px;
        }

        .footer-links a {
            color: #ccc;
        }

        .footer-links a:hover {
            color: var(--accent);
        }

        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }

        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            transition: var(--transition);
        }

        .social-links a:hover {
            background-color: var(--accent);
            transform: translateY(-5px);
        }

        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 0.9rem;
            color: #aaa;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero h1 {
                font-size: 2.8rem;
            }
            
            .about-content,
            .contact-content {
                grid-template-columns: 1fr;
            }
            
            .about-image {
                height: 300px;
                order: -1;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 80px);
                background-color: white;
                flex-direction: column;
                align-items: center;
                padding-top: 40px;
                transition: var(--transition);
            }
            
            .nav-links.active {
                left: 0;
            }
            
            .nav-links li {
                margin: 15px 0;
            }
            
            .mobile-menu-btn {
                display: block;
            }
            
            .hero h1 {
                font-size: 2.3rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .hero-btns {
                flex-direction: column;
                gap: 15px;
            }
            
            .section {
                padding: 60px 0;
            }
        }

        @media (max-width: 576px) {
            .logo h1 {
                font-size: 1.5rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-content">
            <div class="logo">
                <div class="logo-icon">
                    <i class="fas fa-hands-helping"></i>
                </div>
                <h1>Safe Space Kenya</h1>
            </div>
            <button class="mobile-menu-btn">
                <i class="fas fa-bars"></i>
            </button>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#team">Our Team</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container hero-content">
            <h1>Healing Minds, Restoring Lives</h1>
            <p>Safe Space Kenya provides professional, confidential counseling and mental health services in a supportive environment. Our team of licensed therapists is dedicated to helping you navigate life's challenges with compassion and expertise.</p>
            <div class="hero-btns">
                <a href="#contact" class="btn">Book a Session</a>
                <a href="#services" class="btn btn-outline">Our Services</a>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="section" id="services">
        <div class="container">
            <div class="section-header">
                <h2>Our Therapeutic Services</h2>
                <p>We offer a range of evidence-based therapies tailored to meet your individual needs.</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-user-friends fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Individual Counseling</h3>
                        <p>Personalized sessions addressing mental health concerns, emotional challenges, and personal growth.</p>
                        <span class="learn-more" data-service="individual">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-users fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Group Therapy</h3>
                        <p>Supportive group sessions fostering connection and shared healing experiences.</p>
                        <span class="learn-more" data-service="group">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-home fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Family Counseling</h3>
                        <p>Strengthening family bonds and improving communication through guided therapy.</p>
                        <span class="learn-more" data-service="family">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-graduation-cap fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Workshops & Training</h3>
                        <p>Educational programs on mental wellness for organizations and communities.</p>
                        <span class="learn-more" data-service="workshop">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-mobile-alt fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Tele-therapy</h3>
                        <p>Secure online counseling for convenient access to our services.</p>
                        <span class="learn-more" data-service="tele">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-img">
                        <i class="fas fa-hand-holding-heart fa-3x"></i>
                    </div>
                    <div class="service-content">
                        <h3>Trauma Support</h3>
                        <p>Specialized therapy for healing from traumatic experiences and PTSD.</p>
                        <span class="learn-more" data-service="trauma">Learn More <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Detail Modals -->
    <div id="individual-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Individual Counseling</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>Our individual counseling sessions provide a private, confidential space to explore your thoughts, feelings, and challenges with a licensed therapist.</p>
                
                <h4>What to Expect</h4>
                <ul>
                    <li>Personalized sessions tailored to your unique needs</li>
                    <li>Evidence-based therapeutic approaches</li>
                    <li>Safe, non-judgmental environment</li>
                    <li>Development of coping strategies</li>
                    <li>Goal-oriented progress tracking</li>
                </ul>
                
                <h4>Common Issues Addressed</h4>
                <ul>
                    <li>Anxiety and stress management</li>
                    <li>Depression and mood disorders</li>
                    <li>Relationship challenges</li>
                    <li>Grief and loss</li>
                    <li>Self-esteem and identity issues</li>
                    <li>Life transitions and adjustments</li>
                </ul>
                
                <h4>Session Details</h4>
                <p>Initial session: 75 minutes (KSh 3,500)<br>
                Follow-up sessions: 50 minutes (KSh 2,800)<br>
                Packages available for multiple sessions</p>
            </div>
        </div>
    </div>

    <div id="group-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Group Therapy</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>Group therapy provides a supportive environment where individuals with similar experiences come together to share, learn, and heal under professional guidance.</p>
                
                <h4>Benefits of Group Therapy</h4>
                <ul>
                    <li>Shared experiences and mutual support</li>
                    <li>Development of social skills</li>
                    <li>Learning from others' perspectives</li>
                    <li>Reduced feelings of isolation</li>
                    <li>Cost-effective therapeutic option</li>
                </ul>
                
                <h4>Current Group Offerings</h4>
                <ul>
                    <li><strong>Anxiety Management:</strong> Wednesdays, 5:30-7:00 PM</li>
                    <li><strong>Grief Support:</strong> Tuesdays, 4:00-5:30 PM</li>
                    <li><strong>Women's Empowerment:</strong> Saturdays, 10:00-11:30 AM</li>
                    <li><strong>Men's Support Group:</strong> Thursdays, 6:00-7:30 PM</li>
                    <li><strong>Stress Reduction:</strong> Mondays, 5:00-6:30 PM</li>
                </ul>
                
                <h4>Session Details</h4>
                <p>Groups meet weekly for 8-12 week cycles<br>
                Session fee: KSh 1,500 per meeting<br>
                Limited to 8-10 participants per group</p>
            </div>
        </div>
    </div>

    <div id="family-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Family Counseling</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>Family counseling helps family members improve communication, resolve conflicts, and strengthen relationships in a safe, neutral environment.</p>
                
                <h4>Our Approach</h4>
                <ul>
                    <li>Systems-based therapy focusing on family dynamics</li>
                    <li>Conflict resolution strategies</li>
                    <li>Improved communication techniques</li>
                    <li>Strengthening family bonds</li>
                    <li>Addressing generational patterns</li>
                </ul>
                
                <h4>Common Focus Areas</h4>
                <ul>
                    <li>Parent-child relationships</li>
                    <li>Blended family adjustments</li>
                    <li>Divorce and separation support</li>
                    <li>Substance abuse recovery support</li>
                    <li>Cultural differences within families</li>
                    <li>Mental health challenges affecting the family</li>
                </ul>
                
                <h4>Session Details</h4>
                <p>Initial session: 90 minutes (KSh 4,500)<br>
                Follow-up sessions: 60 minutes (KSh 3,500)<br>
                Sliding scale available for families in need</p>
            </div>
        </div>
    </div>

    <div id="workshop-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Workshops & Training</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>We offer educational workshops and training programs designed for organizations, schools, and community groups to promote mental wellness and emotional resilience.</p>
                
                <h4>Popular Workshop Topics</h4>
                <ul>
                    <li>Stress Management in the Workplace</li>
                    <li>Mental Health First Aid Training</li>
                    <li>Building Emotional Resilience</li>
                    <li>Effective Communication Skills</li>
                    <li>Mindfulness and Meditation Practices</li>
                    <li>Conflict Resolution Strategies</li>
                </ul>
                
                <h4>Training Programs</h4>
                <ul>
                    <li><strong>Corporate Wellness:</strong> Half-day and full-day programs tailored to your organization</li>
                    <li><strong>School Programs:</strong> Age-appropriate mental health education for students and teachers</li>
                    <li><strong>Community Workshops:</strong> Accessible mental health education for the public</li>
                    <li><strong>Customized Training:</strong> Programs designed to meet your specific needs</li>
                </ul>
                
                <h4>Pricing</h4>
                <p>Workshops start at KSh 25,000 for up to 20 participants<br>
                Customized training programs available upon request<br>
                Discounts available for non-profits and educational institutions</p>
            </div>
        </div>
    </div>

    <div id="tele-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Tele-therapy</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>Our secure tele-therapy services provide convenient access to professional counseling from the comfort of your home or office.</p>
                
                <h4>How It Works</h4>
                <ul>
                    <li>Secure, HIPAA-compliant video platform</li>
                    <li>Same quality care as in-person sessions</li>
                    <li>Flexible scheduling options</li>
                    <li>Accessible from anywhere in Kenya</li>
                    <li>Easy-to-use technology</li>
                </ul>
                
                <h4>Benefits of Tele-therapy</h4>
                <ul>
                    <li>Convenience and time savings</li>
                    <li>Increased accessibility for those in remote areas</li>
                    <li>Comfort of your own environment</li>
                    <li>No transportation challenges</li>
                    <li>Continuity of care during travel or illness</li>
                </ul>
                
                <h4>Getting Started</h4>
                <ol>
                    <li>Contact us to schedule an appointment</li>
                    <li>Complete intake forms online</li>
                    <li>Receive secure link to your virtual session</li>
                    <li>Connect with your therapist at scheduled time</li>
                </ol>
                
                <p>Session fee: KSh 2,800 for 50-minute session</p>
            </div>
        </div>
    </div>

    <div id="trauma-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Trauma Support</h3>
                <span class="close-btn">&times;</span>
            </div>
            <div class="modal-body">
                <p>Our trauma-informed therapy helps individuals heal from traumatic experiences, PTSD, and related emotional challenges using evidence-based approaches.</p>
                
                <h4>Therapeutic Approaches</h4>
                <ul>
                    <li>Trauma-Focused Cognitive Behavioral Therapy (TF-CBT)</li>
                    <li>Eye Movement Desensitization and Reprocessing (EMDR)</li>
                    <li>Somatic Experiencing</li>
                    <li>Narrative Therapy</li>
                    <li>Mindfulness-Based Stress Reduction</li>
                </ul>
                
                <h4>Who Can Benefit</h4>
                <ul>
                    <li>Survivors of physical or emotional abuse</li>
                    <li>Those experiencing symptoms of PTSD</li>
                    <li>Individuals who have experienced accidents or natural disasters</li>
                    <li>Those who have witnessed violence</li>
                    <li>People dealing with complex or childhood trauma</li>
                </ul>
                
                <h4>Our Approach</h4>
                <p>We create a safe, supportive environment where healing can occur at your own pace. Our therapists are trained in trauma-informed care, focusing on:</p>
                <ul>
                    <li>Safety and trust-building</li>
                    <li>Empowerment and collaboration</li>
                    <li>Cultural sensitivity</li>
                    <li>Understanding trauma's impact on the brain and body</li>
                    <li>Developing healthy coping mechanisms</li>
                </ul>
                
                <p>Initial assessment: KSh 4,000 (90 minutes)<br>
                Ongoing sessions: KSh 3,500 (60 minutes)</p>
            </div>
        </div>
    </div>

    <!-- About Section -->
    <section class="section about" id="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>About Safe Space Kenya</h2>
                    <p>Founded in <strong>2023</strong>, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya. We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions.</p>
                    <p>Our team of licensed therapists brings diverse expertise and a commitment to cultural sensitivity. We provide care that respects the unique backgrounds and experiences of our clients.</p>
                    <p>Confidentiality is fundamental to our practice. We adhere to strict ethical guidelines to ensure your privacy and create a space where you can feel secure to share openly.</p>
                    <a href="#team" class="btn">Meet Our Team</a>
                </div>
                <div class="about-image">
                    <div style="position: relative; z-index: 2;">
                        <i class="fas fa-heart fa-3x"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section class="section" id="team">
        <div class="container">
            <div class="section-header">
                <h2>Our Professional Team</h2>
                <p>Meet our dedicated therapists committed to your mental wellness journey.</p>
            </div>
            <div class="team-grid">
                <div class="team-member">
                    <div class="member-img">
                        <i class="fas fa-user fa-2x"></i>
                    </div>
                    <h3 class="member-name">Jerim Owino</h3>
                    <div class="member-role">Founder & CEO</div>
                    <p>Clinical psychologist specializing in trauma therapy with 12 years of experience. Passionate about accessible mental healthcare.</p>
                </div>
                <div class="team-member">
                    <div class="member-img">
                        <i class="fas fa-user fa-2x"></i>
                    </div>
                    <h3 class="member-name">Hamdi Roble</h3>
                    <div class="member-role">Senior Therapist</div>
                    <p>Expert in cognitive behavioral therapy with focus on anxiety and depression management. MA in Counseling Psychology.</p>
                </div>
                <div class="team-member">
                    <div class="member-img">
                        <i class="fas fa-user fa-2x"></i>
                    </div>
                    <h3 class="member-name">Yvone Orina</h3>
                    <div class="member-role">Family Therapist</div>
                    <p>Specializes in family systems therapy and relationship counseling. Trained in conflict resolution techniques.</p>
                </div>
                <div class="team-member">
                    <div class="member-img">
                        <i class="fas fa-user fa-2x"></i>
                    </div>
                    <h3 class="member-name">Brian Kiprop</h3>
                    <div class="member-role">Art Therapist</div>
                    <p>Uses creative approaches to help clients express and process complex emotions. BA in Psychology and Fine Arts.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="section testimonials" id="testimonials">
        <div class="container">
            <div class="section-header">
                <h2>Client Testimonials</h2>
                <p>Hear what others have to say about their healing journey with us.</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-text">"Safe Space Kenya provided me with the tools to manage my anxiety in a way that respected my cultural background. My therapist was patient, understanding, and genuinely cared about my progress. I'm now living a much fuller life."</p>
                <div class="testimonial-author">- Wanjiru M., Nairobi</div>
            </div>
            <div class="testimonial-card" style="margin-top: 30px;">
                <p class="testimonial-text">"The family counseling sessions helped us rebuild communication after a difficult period. We learned practical tools to express our needs without conflict. Our family is stronger now thanks to Safe Space Kenya."</p>
                <div class="testimonial-author">- David O., Mombasa</div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="section" id="contact">
        <div class="container">
            <div class="section-header">
                <h2>Contact Us</h2>
                <p>Reach out to schedule an appointment or ask questions about our services.</p>
            </div>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div class="contact-text">
                            <h4>Our Location</h4>
                            <p>Greenhouse Plaza, 3rd Floor<br>Ngong Road, Nairobi, Kenya</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-phone-alt"></i>
                        </div>
                        <div class="contact-text">
                            <h4>Phone Number</h4>
                            <p>+254 781 095 919<br>+254 720 987 654</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div class="contact-text">
                            <h4>Email Address</h4>
                            <p>info@safespacekenya.org<br>jerimowino679@gmail.com (CEO)</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <div class="contact-text">
                            <h4>Working Hours</h4>
                            <p>Monday - Friday: 8:00 AM - 7:00 PM<br>Saturday: 9:00 AM - 4:00 PM</p>
                        </div>
                    </div>
                </div>
                <div class="contact-form">
                    <form id="appointment-form">
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input type="text" id="name" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" id="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" class="form-control" placeholder="e.g. +254 781 095 919" required>
                        </div>
                        <div class="form-group">
                            <label for="service">Service Interested In</label>
                            <select id="service" class="form-control" required>
                                <option value="">Select a service</option>
                                <option value="individual">Individual Counseling</option>
                                <option value="group">Group Therapy</option>
                                <option value="family">Family Counseling</option>
                                <option value="workshop">Workshops & Training</option>
                                <option value="tele">Tele-therapy</option>
                                <option value="trauma">Trauma Support</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="message">Your Message</label>
                            <textarea id="message" class="form-control" placeholder="How can we help you?" required></textarea>
                        </div>
                        <button type="submit" class="btn">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-col">
                    <h3>Safe Space Kenya</h3>
                    <p>Providing professional, confidential counseling and mental health services in a supportive environment since 2023.</p>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div class="footer-col">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#services">Services</a></li>
                        <li><a href="#about">About Us</a></li>
                        <li><a href="#team">Our Team</a></li>
                        <li><a href="#testimonials">Testimonials</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Our Services</h3>
                    <ul class="footer-links">
                        <li><a href="#" class="learn-more-footer" data-service="individual">Individual Counseling</a></li>
                        <li><a href="#" class="learn-more-footer" data-service="group">Group Therapy</a></li>
                        <li><a href="#" class="learn-more-footer" data-service="family">Family Counseling</a></li>
                        <li><a href="#" class="learn-more-footer" data-service="workshop">Workshops & Training</a></li>
                        <li><a href="#" class="learn-more-footer" data-service="tele">Tele-therapy</a></li>
                        <li><a href="#" class="learn-more-footer" data-service="trauma">Trauma Support</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Newsletter</h3>
                    <p>Subscribe to our newsletter for mental health tips and updates.</p>
                    <form id="newsletter-form">
                        <div class="form-group">
                            <input type="email" class="form-control" placeholder="Your Email Address" required>
                        </div>
                        <button type="submit" class="btn">Subscribe</button>
                    </form>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2023 Safe Space Kenya. All rights reserved. | Designed with <i class="fas fa-heart" style="color: var(--accent);"></i> for Mental Wellness</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile Menu Toggle
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navLinks = document.querySelector('.nav-links');
        
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // Smooth Scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (navLinks.classList.contains('active')) {
                        navLinks.classList.remove('active');
                        const icon = mobileMenuBtn.querySelector('i');
                        icon.classList.remove('fa-times');
                        icon.classList.add('fa-bars');
                    }
                }
            });
        });
        
        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            if (window.scrollY > 100) {
                header.style.padding = '10px 0';
                header.style.background = 'rgba(255, 255, 255, 0.98)';
            } else {
                header.style.padding = '15px 0';
                header.style.background = 'rgba(255, 255, 255, 0.98)';
            }
        });
        
        // Modal functionality
        const learnMoreBtns = document.querySelectorAll('.learn-more');
        const modals = document.querySelectorAll('.modal');
        const closeBtns = document.querySelectorAll('.close-btn');
        const learnMoreFooter = document.querySelectorAll('.learn-more-footer');
        
        // Open modal
        learnMoreBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const service = btn.getAttribute('data-service');
                document.getElementById(`${service}-modal`).style.display = 'block';
                document.body.style.overflow = 'hidden';
            });
        });
        
        // Footer links open modals
        learnMoreFooter.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const service = link.getAttribute('data-service');
                document.getElementById(`${service}-modal`).style.display = 'block';
                document.body.style.overflow = 'hidden';
            });
        });
        
        // Close modal
        closeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                modals.forEach(modal => {
                    modal.style.display = 'none';
                });
                document.body.style.overflow = 'auto';
            });
        });
        
        // Close modal when clicking outside content
        window.addEventListener('click', (e) => {
            modals.forEach(modal => {
                if (e.target === modal) {
                    modal.style.display = 'none';
                    document.body.style.overflow = 'auto';
                }
            });
        });
        
        // Form submission handling
        document.getElementById('appointment-form').addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you for your message! We will contact you shortly to schedule your appointment.');
            e.target.reset();
        });
        
        document.getElementById('newsletter-form').addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you for subscribing to our newsletter!');
            e.target.reset();
        });
    </script>
</body>
</html>
