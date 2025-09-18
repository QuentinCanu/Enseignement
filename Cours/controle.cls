\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{poly}

\LoadClass{exam}
\pagestyle{headings}

\qformat{\bfseries Exercice \thequestion~:~\thequestiontitle\if@placepoints~(\thepoints)\else\fi\hfill}
\renewcommand{\solutiontitle}{\noindent\textbf{Correction:}\enspace}