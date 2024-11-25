The Digital Competence Framework (DigiComp) "... provides a common framework to assist European citizens and workforce in self-evaluating their skills, setting learning goals, identifying training opportunities, and reaching more and better career opportunities."~[[@europaDigitalCompetence]] It is an international tool for evaluating each person's technology readiness. Multiple versions of this framework exist, with the newest being version 2.2, published in 2022 [[@digi22]]. This version replaces version 2.1, which was published in 2017. [[@DigiCompLevels]]. The main difference between version 2.1 and 2.2 is that "The 2.2 update focuses on "Examples of the knowledge, skills and attitudes applicable to each competence" [[@digi22]], which does not break backwards-compatibility with the previous version and related sources are referring to either of these versions. For this thesis I will use the version interchangeably.

DigiComp comprises five areas and eight proficiency levels. Each of the areas covers a different aspect of working with IT systems, while levels assigned to the areas quantifying the skills of the user in the range from 1 (least-skilled, foundation) to 8 (highly specialized) [[@digi22]][[@DigiCompLevels]]. The DigiComp areas, together with examples of tasks, can be seen in `TEX:\autoref{tab:DigiArea}`. The levels are outlined in `TEX:\autoref{tab:DigiLevel}`  [[@digi22]][[@DigiCompLevels]].

As this framework is supposed to be used on an international level and presents well-defined scales together with examples and explanations, I will use this framework as a reference point for the abilities discussed in user profiles that we can reasonably expect to be present based on existing research and publications. This should make putting this thesis in context with other publications using this scale or directly expanding upon this thesis easier as opposed to developing a custom scale just for this thesis.


```latex
\begin{longtblr}[
  caption = {Areas of Digital Competence v2.2 with examples of tasks for each area \cite{digi22}},
  entry = {Areas of Digital Competence v2.2 with examples of tasks for each area},
  label = {tab:DigiArea}
]{
  colspec = {|p{3cm}|X|},
} 
  Area                            & Example \\
  Information and data literacy   & Browsing, searching, filtering data, information and digital content; Evaluating data, information and digital content; Managing data, information and digital content \\
  Communication and collaboration & Interacting through digital technologies; Sharing through digital technologies; Engaging in citizenship through digital technologies; Collaborating through digital technologies; Netiquette; Managing digital identity \\
  Digital content creation        & Developing digital content; Integrating and re-elaborating digital content; Copyright and licenses; Programming \\
  Safety                          & Protecting devices; Protecting personal data and privacy; Protecting health and well-being; Protecting the environment \\
  Problem solving                 & Solving technical problems; Identifying needs and technological responses; Creatively using digital technologies; Identifying digital competence gaps \\
\end{longtblr}
```


```latex
\begin{longtblr}[
  caption = {Proficiency levels of Digital Competence v2.2 with described properties \cite{digi22,DigiCompLevels}},
  entry = {Proficiency levels of Digital Competence v2.2 with described properties},
  label = {tab:DigiLevel}
]{
  colspec = {|c|p{3cm}|p{3cm}|X|},
} 
Level & Description & Cognitive domain & Autonomy \\
1 & Foundation & Remembering & With guidance \\
2 & Foundation & Remembering & Autonomy and with guidance where needed \\
3 & Intermediate & Understanding & On my own \\
4 & Intermediate & Understanding & Independent and according to my needs \\
5 & Advanced & Applying & Guiding others \\
6 & Advanced & Evaluating & Able to adapt to others in a complex context \\
7 & Highly specialized & Creating & Integrate to contribute to the professional practice and to guide others \\
8 & Highly specialized & Creating & Propose new ideas and processes to the field \\
\end{longtblr}
```

## Mapping to other scales

DigiComp can be considered bulky because it requires providing several scores for several categories. In practice, various available sources often present their own scales, which are not directly related to DigiComp levels but are simplified to just one overall score. Because of that, I have decided to, instead of presenting levels for each of the areas of the DigiComp, specify only one number, which represents a person's average DigiComp level. This simplification does not necessarily mean a significant loss of accuracy. Especially on lower average levels, it can be expected that the individual person has very similar values in all areas, whereas in company settings, multiple employees should specialize in different areas, collectively gaining the final higher level. With that, it should be possible to map level specifications from other sources into the simplified DigiComp. In the sections below, I provide examples of the general public, employees in service and manufacturing companies, and a Czech high school graduate based on existing publications.

### General public proficiency levels

In 2016 [[@OECDSkillsBrief]][[@OECDSkills]]  and 2019 [[@OECDSkillsMatter]], the OEDC  has published a report including the population information and communication technologies (ICT) readiness. This readiness is represented as a portion of a country's population falling into three proficiency levels. The levels on the OECD scale and their best-match mappings into the DigiComp proficiency levels are described [[@OECDSkillsMatter]] in `TEX:\autoref{tab:OECDLevel}`.

For this thesis, I will be using the OECD average level as a point of reference, so this thesis is tailored for a broader audience. In the 2015 policy brief, it is shown that roughly 20 \% of adults have reached OECD level 2 (DigiComp 3) and 5 \% level 3 (DigiComp 6) [[@OECDSkillsBrief]]. The 2019 publication differentiates between young adults (aged 25-34) and older adults (aged 55-65), where approximately 35 \% of younger adults fall into OECD level 2 and 10 \% level 3, while for older adults, these numbers are 8 \% and 2 \% adults respectively. With that, we expect a general audience to be within the DigiComp level range of 2-3, meaning that most adults can perform tasks with which they are familiar on their own.

```latex
\begin{landscape}
\begin{longtblr}[
  caption = {Mapping of OECD proficiency levels \cite{OECDSkillsMatter} into DigiComp levels},
  entry = {Mapping of OECD proficiency levels into DigiComp levels},
  label = {tab:OECDLevel},
]{
  colspec = {|p{1cm}|X|p{1cm}|X|},
} 
OECD Level & OECD Description & DigiComp level & Explanation \\
Level 1 & Complete tasks in which the goal is explicitly stated and for which the necessary operations are performed single and familiar environment. Solve problems in the context of technology-rich environments whose solutions involve a relatively small number of steps, and a limited amount of monitoring across a large number of actions & 2 & Is able to autonomously perform operations, but in a familiar environemnt \\
Level 2 & Complete problems that have explicit criteria for success, a small number of applications, and several steps and operators. Can monitor progress towards a solution and handle unexpected outcomes or impasses. & 3 & Is able to performs tasks on their own, but needs to have the goals expicitly stated \\
Level 3 & Complete tasks involving multiple applications, a large number of steps, impasses, and the discovery and use of ad hoc commands in a novel environment. Establish a plan to arrive at a solution and monitor its implementation as they deal with unexpected outcomes and impasses. & 6 & Is able to select a solution in a complex previously unknown environment. \\
\end{longtblr}
\end{landscape}
```

### Industry and service workers' levels

To obtain a reference point of competencies of employees of a service company profile presented in later chapters, I will use a 2021 paper [[@STEINLECHNER20211185]], which has explored and compared the digital competencies of employees of manufacturing and service-related companies. Furthermore, the author represents their abilities for multiple area dimensions on a 1 to 4 scale of maturity levels, where "the lowest maturity level (Level 1) describes a lack of the focused digital competence and the highest level (Level 4) describes a state of completed development compared to the current state-of-the-art." [[@STEINLECHNER20211185]] As the levels presented inside this article cover almost the same scale as the levels from DigiComp, the mapping of the four levels from this publication into the eight levels of DigiComp can be approximated by multiplying the level by two. Next, by averaging the presented maturity levels, we get to level 2.925 for the service company and 1.875 for the manufacturing company, resulting in 5.85 and 3.75 on the DigiComp scale, respectively. This means that we may expect a relatively high ability of service workers to perform even more complex tasks and for manufacturing workers to use their devices independently.
### Czech high-school absolved level

The Czech Ministry of Education has provided a list of things a high-school insolvent should be capable of regarding their virtual activity [[@DigiCompEduCZ]]. Even though they do not directly provide numbered DigiComp levels, it is possible to assign the most probable DigiComp level to each of the separate items, and take the average level as the overall high school absolvent's DigiComp proficiency level. The items and the assigned closest-match proficiency levels from DigiComp can be seen in `TEX:\autoref{tab:HSLevels}`.

The resulting overall rounded proficiency level is 4, which can be translated to a person who is independent in using technologies and can adapt them according to their needs.

```latex
\begin{longtblr}[
  caption = {Abilities of Czech high school absolvent \cite{DigiCompEduCZ} with assigned DigiComp proficiency levels},
  entry = {Abilities of Czech high school absolvent with assigned DigiComp proficiency levels},
  label = {tab:HSLevels},
]{
  colspec = {|X|p{8ex}|p{3cm}|},
}
Absolvent’s ability & Assigned Level & Explanation \\
... is proficient with the necessary set of digital devices, applications and services, using them in school work and in public life; adjusts and changes digital technologies and their use as available options evolve and as their own needs change & 4 & Independent in usage of technologies \\
... acquires, assesses, manages, shares and communicates data, information and digital content in a variety of formats; to do so, chooses processes, strategies and methods that are appropriate to the specific situation and purpose & 5-6 & Evaluates the best solution \\
... creates, enhances and connects digital content in different formats; expresses themselves using digital means & 4-5 & Is able to creatively apply knowledge for personal tasks \\
... proposes solutions through digital technologies to improve processes or technologies; can advise on technical problems & 5 & Is able to guide others in non-professional settings \\
... deals with the variability of digital technologies and assesses how developments in technology affect different aspects of individual and societal life and the environment, weighing up the risks and benefits & 4 & Is able to customize the new technologies to their needs \\
... avoid situations that threaten the security of equipment and data, and situations that threaten their physical and mental health; act ethically, with consideration and respect for others when collaborating, communicating and sharing information in a digital environment & 3 & Does understand learned methods of data security and protection on their own \\
\end{longtblr}
```
