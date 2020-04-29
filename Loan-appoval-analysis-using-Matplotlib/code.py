# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

#Code starts here
loan_status = data['Loan_Status'].value_counts()

plt.bar(loan_status.index,loan_status)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(10,5))

plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)





# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar',stacked=True, figsize=(10,5))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)






# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density' ,label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1,figsize=(10,5))

data.plot.scatter(x='ApplicantIncome', y='LoanAmount')
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome', y='LoanAmount')
ax_2.set_title('Coapplicant Income')

#New Column
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Axis 3
data.plot.scatter(x='TotalIncome', y='LoanAmount')
ax_3.set_title('Total Income')





