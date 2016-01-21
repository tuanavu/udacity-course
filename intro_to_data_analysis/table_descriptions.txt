enrollments.csv:

Data about a random subset of Data Analyst Nanodegree students who complete
their first project and a random subset of students who do not.

Columns:
   - account_key:    A unique identifier for the account of the student who
                     enrolled.

    - status:         The enrollment status of the student at the time the data
                      was collected. Possible values are 'canceled' and
                      'current'.

    - join_date:      The date the student enrolled.

    - cancel_date:    The date the student canceled, or blank if the student has
                      not yet canceled.

    - days_to_cancel: The number of days between join_date and cancel_date, or
                      blank if the student has not yet canceled.

    - is_udacity:     True if the account is a Udacity test account, False
                      otherwise.

    - is_canceled:    True if the student had canceled this enrollment at the
                      time the data was collected, False otherwise.

-------------------------------------------------------------------------------

daily_engagement.csv:

Data about engagement within Data Analyst Nanodegree courses for each student in
the enrollment table on each day they were enrolled. Includes a record even if
there was no engagement that day. Includes engagement data from both the
supporting courses for the Nanodegree program, and the corresponding freely
available courses with the same content.

Columns:
    - acct:                  A unique identifier for the account of the student
                             whose engagement data this is.

    - utc_date:              The date for which the data was collected.

    - num_courses_visited:   The total number of Data Analyst Nanodegree courses
                             the student visited for at 2 minutes on this day.
                             Nanodegree courses and freely available courses
                             with the same content are counted separately.

    - total_minutes_visited: The total number of minutes the student spent
                             taking Data Analyst Nanodegree courses on this day.

    - lessons_completed:     The total number of lessons within Data Analyst
                             Nanodegree courses on this day.

    - projects_completed:    The total number of Data Analyst Nanodegree
                             projects the student completed on this day.

-------------------------------------------------------------------------------

project_submissions.csv:

Data about submissions for Data Analyst Nanodegree projects for each student in
the enrollment table.

Columns:
    - creation_date:    The date the project was submitted.

    - completion_date:  The date the project was evaluated.

    - assigned_rating:  This column has 4 possible values:
                        blank - Project has not yet been evaluated.
                        INCOMPLETE - Project did not meet specifications.
                        PASSED - Project met specifications.
                        DISTINCTION - Project exceeded specifications.
                        UNGRADED - The submission could not be evaluated
                                   (e.g. contained a corrupted file)

    - account_key:      A unique identifier for the account of the student who
                        submitted the project.

    - lesson_key:       A unique identifier for the project that was submitted.

    - processing_state: This column has 2 possible values:
                        CREATED - Project has been submitted but not evaluated.
                        EVALUATED - Project has been evaluated.

-------------------------------------------------------------------------------

daily_engagement_full.csv:

Similar to daily_engagement.csv, but with engagement further broken down by
course and with more columns available. This file is about 500 megabytes, which
is why the smaller daily_engagement.csv file was created. This dataset is
optional; it is not needed to complete the course.

In addition to the following columns, this table also contains all the same
columns as daily_engagement.csv, except with has_visited instead of
num_courses_visited.

Columns:
    - registration_date:  Date the account was registered.

    - subscription_start: Date paid subscription for the account started.

    - course_key:         Course in which activity is recorded.

    - sibling_key:        Free course with the same free content as course_key.
                          If course_key is a free course, course_key and
                          sibling_key are the same.

    - course_title:       Title of the course.

    - has_visited:        1 if the student visited this course for at least 2
                          minutes on this day.

