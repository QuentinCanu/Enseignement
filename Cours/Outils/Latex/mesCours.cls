\NeedsTexFormat{LaTeX2e}
\ProvidesClass{mesCours}[2024-03-27 Classes pour mes cours]

\LoadClassWithOptions{article}
\RequirePackage[T1]{fontenc}
\RequirePackage[french]{babel}
\RequirePackage{mathtools,amsmath,amssymb,amsthm}
\RequirePackage{tikz,tkz-tab}
\RequirePackage{cleveref}
\RequirePackage{enumitem}
\RequirePackage{multicol}
\RequirePackage{eurosym}
\RequirePackage{url}
\RequirePackage{lcg}
\RequirePackage{multido}
\RequirePackage{array}
\RequirePackage{titling}
\RequirePackage{siunitx}
\RequirePackage{xspace}
\RequirePackage{pdfpages}
\RequirePackage{caption}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage[a4paper,margin=2cm]{geometry}

\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\D}{\mathbb{D}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newtheorem{definition}{Définition}
\newtheorem{proposition}{Proposition}
\newtheorem*{remark}{Remarque}
\newtheorem*{vocabulary}{Vocabulaire}
\newtheorem*{example}{Exemple}

\newcommand{\vect}[1]{\overrightarrow{#1}}
\newcommand{\function}[5]{\begin{array}[t]{lrcl}
#1\colon & #2 & \longrightarrow & #3 \\
    & #4 & \longmapsto & #5 \end{array}}

\newcommand{\millirepere}{}
\def\millirepere[#1](#2,#3) -- (#4,#5){%
\draw[very thin] (#2,#3) grid[#1] (#4,#5);
\draw[ultra thick, ->] (#2,0) -- (#4,0) node[above left] {$x$};
\draw[ultra thick, ->] (0,#3) -- (0,#5) node[below right] {$y$};
}

\newcommand{\qformatExam}{\qformat{\textbf{Exercice \thequestion : \thequestiontitle} (\thepoints)\hfill}}

\newcommand{\random}[2]{\chgrand[first=#1, last=#2]\rand\arabic{rand}}

\newcommand{\emptybox}[2][\textwidth]{%
  \begingroup
  \setlength{\fboxsep}{-\fboxrule}%
  \noindent\framebox[#1]{\rule{0pt}{#2}}%
  \endgroup
}

\DeclareOption{poly}{
\pagestyle{fancy}
\rhead{\theauthor}
\lhead{\thetitle}
\chead{}
\lfoot{}
\cfoot{}
\rfoot{\thepage}
}
\DeclareOption{exam}{
\LoadClass{exam}
\qformat{\textbf{Exercice \thequestion : \thequestiontitle} (\thepoints)\hfill}
}
\DeclareOption{exos}{
\LoadClass{exam}
\qformat{\textbf{Exercice \thequestion :}\hfill}
}
\ProcessOptions\relax