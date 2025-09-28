\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{poly}

\LoadClass{exam}
\pagestyle{headings}
\RequirePackage{geometry}
\geometry{top=2cm}

\qformat{\bfseries Exercice \thequestion~:~\thequestiontitle\if@placepoints~(\thepoints)\else\fi\hfill}
\renewcommand{\solutiontitle}{\noindent\textbf{Correction:}\enspace}