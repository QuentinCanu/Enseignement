\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{poly}

\LoadClass{exam}
\pagestyle{headings}
\RequirePackage{geometry}
\geometry{top=2cm}

\qformat{\bfseries Exercice \thequestion~:~\thequestiontitle\if@placepoints~(\thepoints)\else\fi\hfill}
\renewcommand{\solutiontitle}{\noindent\textbf{Correction:}\enspace}

\newcommand{\instructions}[1][Interdite]{
\begin{tcolorbox}
\begin{itemize}
\item Tout effort de recherche, même non abouti, sera valorisé.
\item Les exercices sont indépendants, et peuvent être faits dans l'ordre de votre choix.
\item Sauf mention contraire, toute réponse devra être justifiée.
\item L'utilisation de la calculatrice est \textbf{#1}.
\end{itemize}
\end{tcolorbox}
}