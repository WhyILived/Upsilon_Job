import requests
import json

# URL of the local Flask server
URL = 'http://localhost:5000/api/render-latex'

# Minimal LaTeX document
latex_code = r'''
\documentclass[11pt, letterpaper]{article}

% Packages:
\usepackage[
    ignoreheadfoot, % set margins without considering header and footer
    top=1.2 cm, % seperation between body and page edge from the top
    bottom=0.8 cm, % seperation between body and page edge from the bottom
    left=1 cm, % seperation between body and page edge from the left
    right=1 cm, % seperation between body and page edge from the right
    footskip=1.0 cm, % seperation between body and footer
    % showframe % for debugging 
]{geometry} % for adjusting page geometry
\usepackage{titlesec} % for customizing section titles
\usepackage{tabularx} % for making tables with fixed width columns
\usepackage{array} % tabularx requires this
\usepackage[dvipsnames]{xcolor} % for coloring text
\definecolor{primaryColor}{RGB}{0, 79, 144} % define primary color
\definecolor{cHead}{RGB}{73,96,164} % custom header color
\usepackage{enumitem} % for customizing lists
\usepackage{fontawesome5} % for using icons
\usepackage{lmodern}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault} % Switches to a sans-serif font
\usepackage{amsmath} % for math
\usepackage[dvipsnames]{xcolor} % for color
\usepackage[
    pdftitle={Mushfiqur Shadhin's CV},
    pdfauthor={Mushfiqur Shadhin},
    pdfcreator={LaTeX with RenderCV},
    colorlinks=true,
    urlcolor=primaryColor
]{hyperref} % for links, metadata and bookmarks
\usepackage[pscoord]{eso-pic} % for floating text on the page
\usepackage{calc} % for calculating lengths
\usepackage{bookmark} % for bookmarks
\usepackage{changepage} % for one column entries (adjustwidth environment)
\usepackage{paracol} % for two and three column entries
\usepackage{ifthen} % for conditional statements
\usepackage{needspace} % for avoiding page brake right after the section title
\usepackage{iftex} % check if engine is pdflatex, xetex or luatex
% Ensure that generate pdf is machine readable/ATS parsable:
\ifPDFTeX
    \input{glyphtounicode}
    \pdfgentounicode=1
    % \usepackage[T1]{fontenc} % this breaks sb2nov
    \usepackage[utf8]{inputenc}
    \usepackage{lmodern}
\fi



% Some settings:
\AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment
\pagestyle{empty} % no header or footer
\setcounter{secnumdepth}{0} % no section numbering
\setlength{\parindent}{0pt} % no indentation
\setlength{\topskip}{0pt} % no top skip
\setlength{\columnsep}{0cm} % set column seperation
\makeatletter
\makeatother

\titleformat{\section}{\needspace{0\baselineskip}\bfseries\large\color{cHead}}{}{0pt}{}[\vspace{-8pt}\rule{\textwidth}{2pt}]

\titlespacing{\section}{
    % left space:
    -1pt
}{
    % top space:
    0.2 cm
}{
    % bottom space:
    0.1 cm
} % section title spacing

\renewcommand\labelitemi{$\circ$} % custom bullet points
\newenvironment{highlights}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=3pt,
        leftmargin=0.4 cm + 10pt
    ]
}{
    \end{itemize}
} % new environment for highlights

\newenvironment{highlightsforbulletentries}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=10pt
    ]
}{
    \end{itemize}
} % new environment for highlights for bullet entries


\newenvironment{onecolentry}{
    \begin{adjustwidth}{
        0.0 cm + 0.00001 cm
    }{
        0.0 cm + 0.00001 cm
    }
}{
    \end{adjustwidth}
} % new environment for one column entries

\newenvironment{twocolentry}[2][]{
    \onecolentry
    \def\secondColumn{#2}
    \setcolumnwidth{\fill, 4.5 cm}
    \begin{paracol}{2}
}{
    \switchcolumn \raggedleft \secondColumn
    \end{paracol}
    \endonecolentry
} % new environment for two column entries

\newenvironment{header}{
    \setlength{\topsep}{0pt}\par\kern\topsep\centering\linespread{1.5}
}{
    \par\kern\topsep
} % new environment for the header


% save the original href command in a new command:
\let\hrefWithoutArrow\href

% new command for external links:
\renewcommand{\href}[2]{\hrefWithoutArrow{#1}{\ifthenelse{\equal{#2}{}}{ }{#2 }\raisebox{.15ex}{\footnotesize \faExternalLink*}}}


\begin{document}
    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{}

    \begin{header}
        \textbf{\fontsize{24 pt}{24 pt}\selectfont \color{cHead}Mushfiqur Shadhin}

        \vspace{0.3 cm}

        \normalsize
        \mbox{\hrefWithoutArrow{mailto:mm22rahm@uwaterloo.ca}{\color{black}{\footnotesize\faEnvelope[regular]}\hspace*{0.13cm}mm22rahm@uwaterloo.ca}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{\hrefWithoutArrow{tel:+1 548 384-5520}{\color{black}{\footnotesize\faPhone*}\hspace*{0.13cm}+1 (548) 384-5520}}%
        \kern 0.25 cm%
        \AND%
        \kern 0.25 cm%
        \mbox{\hrefWithoutArrow{https://www.linkedin.com/in/mushfiqur-shadhin-06b084308/}{\color{black}{\footnotesize\faLinkedinIn}\hspace*{0.13cm}linkedin.com/in/mushfiqur-shadhin}}%
        \kern 0.25 cm%
    \end{header}

    \vspace{0.3 cm - 0.3 cm}


    \section{TECHNICAL SKILLS}



        
        \begin{onecolentry}
            \fontdimen2\font=0.5ex% inter word space
            \textbf{Languages:} C++, C, Python, Java, Julia, Lua, Kotlin, SQL, MATLAB\\
            \textbf{Technologies:} React, Flask, Docker, pyTorch, OpenCV, sklearn, GCP, Git, Azure, AWS, CUDA, .NET, Node.js, Flutter
        \end{onecolentry}


    \section{PROJECTS}



        
        \begin{twocolentry}{
            
            
        \textit{\href{https://www.thedailystar.net/campus/news/first-hybrid-rocket-engine-bangladesh-tested-successfully-3418016}{\textbf{thedailystar [news]}}}}
            \textbf{Hybrid Rocket Engine (Research-Grade)} $|$ \textit{C++, Python,  MATLAB}
        \end{twocolentry}
        
        \vspace{0.15 cm}
        
        \begin{onecolentry}
            \begin{highlights}

                \item  Achieved \textbf{20,000\%} greater thrust through implementing throttling \textbf{accuracy} through creating algorithms using \textbf{sensor} \textbf{fusion} input, implemented using \textbf{C++}.

                \item Developed \textbf{hot-fire} \textbf{control} \textbf{systems} consisting of \textbf{46} \textbf{components} to increase operating range by \textbf{15km} and safety by over \textbf{97\%} using \textbf{FDI} \& \textbf{FMEA} \textbf{algorithms} coded in \textbf{C++} \& \textbf{Python} through \textbf{Teensy} and \textbf{NodeMCU}.

                \item Modeled \textbf{fuel} \textbf{regression}, \textbf{nozzle} \textbf{wear} \& \textbf{chamber} \textbf{pressure} from \textbf{13} \textbf{sensors} creating sensor fusion which increased final thrust \mbox{accuracy} by an \textbf{additional} \textbf{x18\%} using \textbf{Unscented} \textbf{Kalman} \textbf{Filters} coded in \textbf{MATLAB}.

            \end{highlights}
        \end{onecolentry}
        
        \vspace{0.2 cm}
        
        \begin{twocolentry}{
            
            
        \textit{\href{https://www.dhakatribune.com/bangladesh/education/336482/aiub-aerd-to-launch-its-first-weather-balloon}{\textbf{dhakatribune [news]}}}}
            \textbf{Modular Weather Balloon (Research-Grade)} $|$ \textit{C++, Python, OpenCV, SQL, RPi}
        \end{twocolentry}

        \vspace{0.15 cm}
        
        \begin{onecolentry}
            \begin{highlights}

                \item Engineered a weather balloon with \textbf{real}\textbf{-time} \textbf{location} \textbf{tracking} over \textbf{130km}, \textbf{data} \textbf{processing} of up to \textbf{18} \textbf{sensors} and \textbf{mapping} of \textbf{$\approx$ 42km²} using \textbf{SLAM} \mbox{\textbf{algorithms}} coded using \textbf{C++} in \textbf{OpenCV} on \textbf{RPi}.

                \item Designed \textbf{real-time} \textbf{long-range} transmission to achieve \textbf{radio} \textbf{communication} within \textbf{18km} \textbf{radius} and \textbf{cellular} \textbf{coverage} of around \textbf{150,000 km²} using \textbf{LoRa} \& \textbf{GSM} communcation coded with \textbf{C++} \& \textbf{AT} commands.
            \end{highlights}
        \end{onecolentry}

        \vspace{0.2 cm}

        \begin{twocolentry}{
            
            
        \textit{\href{https://studenthub.cloud}{\textbf{studenthub [website]}}}}
            \textbf{Online Educational Platform} $|$ \textit{Svelte, Typescript, CSS, Javascript, HTML}
        \end{twocolentry}

        \vspace{0.15 cm}

        \begin{onecolentry}
            \begin{highlights}
                \item Developed a \textbf{web-based} \textbf{note-sharing} platform for high school students, hosting websites for \textbf{TEDx} \& \textbf{MUN}, supporting up to \textbf{13,000} \textbf{users} at peak using \textbf{Svelte}, \textbf{HTML}, \textbf{CSS}, \textbf{JavaScript}, and \textbf{TypeScript}.
                \item As \textbf{CEO}, led \textbf{9} \textbf{teams} of $\approx$ \textbf{200} \textbf{members} (web dev, legal, graphic design, among others) to achieve school-wide extracurricular \textbf{awards} through a \textbf{6-month} \textbf{plan} using \textbf{Notion}, weekly meetings, and \textbf{seminars}.
            \end{highlights}
        \end{onecolentry}
        
        \vspace{0.2 cm}

    
    \section{EXPERIENCE}

        \begin{twocolentry}{
        \textit{Aug 2024 – Present}}
            \textbf{Georgia Tech} $|$ \textbf{Member at Propulsive Landers - Firmware Engineer}
        \end{twocolentry}

        \vspace{0.15 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Programmed a \textbf{low-level} \textbf{firmware} for stabilization controls in \textbf{VTOL}, integrating \textbf{16} \textbf{sensors} to achieve \textbf{$>$70\%} \textbf{increase} in \textbf{vector} \textbf{stabilization} coded in \textbf{C} using \textbf{SPI}/\textbf{I2C} \textbf{protocols}.

                \item Designed a \textbf{microcontroller} \textbf{framework} to support \textbf{VTOL} operations with \textbf{real-time} \textbf{feedback} optimizing control loops for \textbf{55\%} \textbf{more} \textbf{responsiveness} to enable smoother vertical lift transition using \textbf{FreeRTOS} \& \textbf{JTAG}.
            \end{highlights}
        \end{onecolentry}

        \vspace{0.2 cm}
        
        \begin{twocolentry}{
        \textit{Apr 2023 – Oct 2024}}
            \textbf{AERD} $|$ \textbf{Head of A\&GNC - Embedded Systems Engineer \& Software Engineer}
        \end{twocolentry}

        \vspace{0.15 cm}
        \begin{onecolentry}
            \begin{highlights}

                \item Gained \textbf{wide} \textbf{media} \textbf{recognition} in \textbf{45} \textbf{news outlets} \href{https://docs.google.com/spreadsheets/d/1mh5iQQR3VqEasFa7Z4QFntadz3Chmxj6hpbO-XVsYfw/edit?usp=sharing}{\textbf{[\textit{excel sheet}]}} and \textbf{$\approx$ 30} \textbf{TV} \textbf{broadcasts} through conducting \textbf{seminars} in \textbf{universities} and participating in \textbf{media} \textbf{interviews}.
            
                \item Developed rocket \textbf{flight} \textbf{computers} with \textbf{active} \textbf{fin} \textbf{stabilization} from a \textbf{9DOF} \textbf{IMU} improving in-flight oscillations by \textbf{87\%} compared to passive systems. used \textbf{PID} \textbf{algorithm} coded in \textbf{C++} through \textbf{ESP32} \& \textbf{Teensy}.
                
                \item Made \textbf{on-board} flight prediction models which achieved \textbf{trajectory} \textbf{forecasts} with \textbf{92\%} \textbf{accuracy} and \textbf{reduced} \textbf{potential} \textbf{flight} \textbf{risks} by above \textbf{70\%} by implementing \textbf{MDP} \textbf{algorithms} coded in \textbf{Python} using \textbf{RocketPy}.
                
            \end{highlights}
        \end{onecolentry}

        \vspace{0.2 cm}


    \section{EDUCATION}
        
        \begin{twocolentry}{      
        2024 - 2029\\
        \textit{Waterloo, ON}}
            \textbf{University of Waterloo}\\
            \textit{BASc in Computer Engineering}
        \end{twocolentry}
\end{document}T
'''

payload = {
    'latex': latex_code
}

response = requests.post(URL, json=payload)

print('Status code:', response.status_code)
try:
    print('Response:', response.json())
except Exception:
    print('Raw response:', response.text) 